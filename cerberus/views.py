from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileSerializer, UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
import logging

logger = logging.getLogger(__name__)



@api_view(['POST'])
def login(request):
    try:
        user  = User.objects.get(email=request.data['email'])
        if not user.check_password(request.data['password']):
            return Response({'error':'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        token,created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK  )
    except User.DoesNotExist:
        return Response({'error':'User Not Found'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.is_staff = False
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def activate(request):
    user = User.objects.get(id=request.data['id'])
    user.is_staff = True
    user.save()
    return Response({'message':'User activated'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def profile(request):
    serializer = ProfileSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated,IsAdminUser])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def getNotStaffUsers(request):
    users = User.objects.filter(is_staff=False)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

