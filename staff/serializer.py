from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

class StructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Structure
        fields = "__all__"

class PostitonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']