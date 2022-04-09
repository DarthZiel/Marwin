from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializer import *
from .models import *
# Create your views here.
class StaffApiList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class StructureApiList(generics.ListAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer
    permission_classes = (IsAuthenticated ,)
class PositionApiList(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PostitonSerializer
    permission_classes = (IsAuthenticated,)


class StaffUpdate(generics.RetrieveUpdateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAuthenticated,)
class StaffDestroy(generics.RetrieveDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = (IsAuthenticated,)

class StructureUpdate(generics.RetrieveUpdateAPIView):
    queryset = Structure.objects.all()
    serializer_class = StructureSerializer
    permission_classes = (IsAuthenticated,)
class StructureDestroy(generics.RetrieveDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StructureSerializer
    permission_classes = (IsAuthenticated,)
class PositionUpdate(generics.RetrieveUpdateAPIView):
    queryset = Position.objects.all()
    serializer_class = PostitonSerializer
    permission_classes = (IsAuthenticated,)
class PositionDestroy(generics.RetrieveDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PostitonSerializer
    permission_classes = (IsAuthenticated,)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDelete(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


