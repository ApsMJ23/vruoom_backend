from rest_framework import serializers
from dionysus.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['businessName','address','GSTIN','SAPCode','PAN','YearOfEstablishment','TypeOfFirm','TypeOfSite']

class SaveClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['businessName','address','GSTIN','SAPCode','PAN','YearOfEstablishment','TypeOfFirm','TypeOfSite','vruoomAdminId']        