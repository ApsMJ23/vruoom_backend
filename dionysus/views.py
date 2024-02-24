from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

from cerberus.serializers import ProfileSerializer
from dionysus.serializers import ClientSerializer
from dionysus.serializers import SaveClientSerializer
from dionysus.models import Client

# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def getClientList(request):
    userSerializer = ProfileSerializer(instance=request.user)
    clientList = Client.objects.filter(vruoomAdminId=request.user.id)
    clientSerializer = ClientSerializer(clientList, many=True)
    if len(clientSerializer.data) == 0:
        return Response({"message":"No clients found"}, status=404)
    return Response({"data":clientSerializer.data}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, SessionAuthentication])
def addClient(request):
    userSerializer = ProfileSerializer(instance=request.user)
    data = request.data
    data['vruoomAdminId'] = userSerializer.data['id']
    clientSerializer = SaveClientSerializer(data=data)
    if clientSerializer.is_valid():
        clientSerializer.save()
        return Response({"message":"Client added successfully"}, status=201)
    return Response(clientSerializer.errors, status=400)

