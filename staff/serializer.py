from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
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