from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files")

    def __str__(self):
        return "User : %s , File Name : %s " % (self.user, self.name)

    class Meta:
        ordering = ("id",)
