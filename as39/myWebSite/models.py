from django.db import models

# Create your models here.



class Student(models.Model):
    stuid =models.IntegerField()
    stuname = models.CharField(max_length=60)
    stuemail = models.EmailField(max_length=60)
    stupass = models.CharField(max_length=50)
    comment = models.CharField(max_length=40, default='not available')
    def __str__(self):
        return str(self.stuid)