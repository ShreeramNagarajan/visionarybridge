from django.db import models

class database(models.Model):
    Name=models.CharField(max_length=40)
    Email=models.EmailField(unique=True)
    Mobile_no=models.CharField(max_length=12)
    Resume=models.FileField(upload_to='resume/')

    def __str__(self) :
        return self.Name


