from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Portal(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.DecimalField(decimal_places=2, max_digits=10)


    def __str__(self):
        return self.title

