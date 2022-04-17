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
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
user_router = routers.SimpleRouter()
user_router.register(r'user', UserViewSet)

profile_router = routers.SimpleRouter()
profile_router.register(r'profile', ProfileViewSet)

position_router = routers.SimpleRouter()
position_router.register(r'position', PostitonViewSet)

structure_router = routers.SimpleRouter()
structure_router.register(r'structure', StructureViewSet)
# Дамир, тут все просто.
# http://127.0.0.1:8000/ + profile или user или position или structure/ , если нужна отельная запись, то тоже самое, но + /id
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('staff.urls')),
    path('api/v1/', include(user_router.urls)),
    path('api/v1/', include(profile_router.urls)),
    path('api/v1/', include(profile_router.urls)),]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)