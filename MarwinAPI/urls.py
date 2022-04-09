"""MarwinAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from staff.views import *
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/stafflist', StaffApiList.as_view()),
    path('api/structurelist', StructureApiList.as_view()),
    path('api/postionlist', PositionApiList.as_view()),
    path('api/StaffUpdate/<int:pk>',StaffUpdate.as_view()),
    path('api/StaffDestroy/<int:pk>', StaffDestroy.as_view()),
    path('api/StructureUpdate/<int:pk>', StructureUpdate.as_view()),
    path('api/StructureDestroy/<int:pk>', StructureDestroy.as_view()),
    path('api/PostitonUpdate/<int:pk>',PositionUpdate.as_view()),
    path('api/PositionDestroy/<int:pk>', PositionDestroy.as_view()),
    path('api/UserList/',UserList.as_view()),
    path('api/UserDetail/<int:pk>', UserDetail.as_view()),
    path('api/UserDelete/<int:pk>', UserDelete.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
]
