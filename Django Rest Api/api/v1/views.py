from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.decorators import action

from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UploadedFilesViewSet(viewsets.ModelViewSet):
    queryset = models.UploadedFile.objects.all()
    serializer_class = serializers.UploadedFilesSerializer
