from django.db import models

# Create your models here.
class Health(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact = models.CharField(max_length=100)
    diagnosis = models.CharField(max_length=100)
    admission_date = models.DateField()

    def __str__(self):
        return self.name