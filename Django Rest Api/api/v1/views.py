from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response


from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(detail=False, methods=["get"])
    def login_auth(self, request, *args, **kwargs):
        
        if request.GET.get("username") and request.GET.get("password"):
            username=request.GET["username"]
            password=request.GET["password"]
            user_obj=User.objects.filter(username=username).first()
            if user_obj:
                match_check = check_password(password,user_obj.password)
                if match_check:
                    return Response(user_obj.id)
                else:
                    return Response(0,status=404)
            else:
                return Response(0, status=404)        
        else:
            return Response(0)



class UploadedFilesViewSet(viewsets.ModelViewSet):
    queryset = models.UploadedFile.objects.all()
    serializer_class = serializers.UploadedFilesSerializer
