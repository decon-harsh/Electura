from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="files")
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)
    
    class Meta():
        ordering = ('id',)        
    
