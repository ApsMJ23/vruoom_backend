from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from cerberus.serializers import ProfileSerializer
from dionysus.serializers import ClientSerializer
from dionysus.models import Client

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def getClientList(request):
    userSerializer = ProfileSerializer(instance=request.user)
    clientList = Client.objects.filter(vruoomAdminId=request.user.id)
    clientSerializer = ClientSerializer(clientList, many=True)
    return Response({"data":clientSerializer.data}, status=200)

