from django.urls import path, include
from django.conf.urls import url

from rest_framework import routers, permissions

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet,basename="User")
router.register('uploaded_files', views.UploadedFilesViewSet,basename="Uploaded Files")

urlpatterns = [
    path('v1/', include(router.urls)),
]