from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
SEX = [('мужчина', 'мужчина'), ('женщина','женщина')]
class Profile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=100)
    postiton = models.ForeignKey("Position", on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='дата рождения')
    structure = models.ForeignKey('Structure', on_delete=models.CASCADE)
    nation = models.CharField(max_length=100)
    iin = models.CharField(max_length=12)
    adress = models.CharField(max_length=100, verbose_name='адрес')
    photo = models.ImageField()
    citizenship = models.CharField(max_length=100, verbose_name='гражаданство')
    experience = models.CharField(max_length=100, verbose_name='стаж')
    sex =  models.CharField(max_length=100,choices=SEX, verbose_name='пол')
    militaryID = models.BooleanField(default=True)
    Type_of_education = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    Couses = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    diploma = models.FileField()
class Position(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Structure(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

