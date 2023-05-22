from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=25)
    instructor=models.CharField(max_length=25)
    duration = models.CharField(max_length=25)

    def __str__(self):
        return self.title



