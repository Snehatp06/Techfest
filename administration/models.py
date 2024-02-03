from django.db import models

# Create your models here.
class program(models.Model):
    program_no = models.IntegerField(primary_key=True)
    program_name = models.CharField(max_length=50)
    date=models.CharField(max_length=20)
    venue=models.CharField(max_length=100)
    discription=models.CharField(max_length=250)
    terms_condition=models.CharField(max_length=300)
    img=models.ImageField(upload_to='gallery')
    

    def __str__(self):
        return self.program_name
