from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','isAdmin']

    def get_isAdmin(self, obj):
        return obj.is_superuser


class ProfileSerializer(serializers.ModelSerializer):
    isAdmin = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = ['id','username','email','is_staff','first_name','last_name','isAdmin']

    def get_isAdmin(self, obj):
        return obj.is_superuser