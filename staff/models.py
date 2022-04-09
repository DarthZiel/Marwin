from django.db import models

# Create your models here.
class Staff(models.Model):
    Fio = models.CharField(max_length=100)
    positon = models.ForeignKey('Position', on_delete=models.CASCADE)
    structure = models.ForeignKey('Structure', on_delete=models.CASCADE)
    def __str__(self):
        return self.Fio

class Position(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Structure(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

