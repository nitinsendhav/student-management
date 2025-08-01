from django.db import models

class studentModel(models.Model):
    name = models.CharField(max_length=90)
    subject = models.CharField(max_length=50, null=True, blank=True)
    roll = models.CharField(max_length=20, null=True, blank=True)
    marks = models.CharField(max_length=10, null=True, blank=True)
    grade = models.CharField(max_length=10, null=True, blank=True)
    result = models.CharField(max_length=10,null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name} - {self.roll}"
  
  