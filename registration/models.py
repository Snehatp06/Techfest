from django.db import models

# Create your models here.

class participant(models.Model):
    participant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email=models.EmailField()
    password = models.CharField(default="NULL",max_length=20)
    participant_ph = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    college=models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

