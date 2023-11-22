from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    descptn=models.TextField()

    def __str__(self):
            return self.name

class Team(models.Model):
    name1=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pict')
    about=models.TextField()

    def __str__(self):
        return self.name1
