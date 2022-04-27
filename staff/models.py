from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
EDUCATION = [
    ('Высшее', 'Высшее'), ('ср-спе', 'Среднее-специальное'), ('среднее', 'Среднее')
]
SEX = [('мужчина', 'мужчина'), ('женщина','женщина')]
class Profile(models.Model):

    fio = models.CharField(max_length=100)
    position = models.ForeignKey("Position", on_delete=models.CASCADE,blank=True)
    date_of_birth = models.DateField(verbose_name='дата рождения')
    structure = models.ForeignKey('Structure', on_delete=models.CASCADE,blank=True)
    nation = models.ForeignKey('nation', max_length=100, on_delete=models.DO_NOTHING)
    iin = models.CharField(max_length=12)
    adress = models.CharField(max_length=100, verbose_name='адрес')
    photo = models.ImageField(blank=True)
    citizenship = models.CharField(max_length=100, verbose_name='гражаданство')
    experience = models.CharField(max_length=100, verbose_name='стаж')
    sex = models.CharField(max_length=100,choices=SEX, verbose_name='пол')
    militaryID = models.BooleanField(default=True)
    Type_of_education = models.CharField(max_length=100, choices=EDUCATION)
    Qualification = models.CharField(max_length=100)
    Courses = models.CharField(max_length=100)
    speciality = models.CharField(max_length=100)
    diploma = models.FileField(blank=True)
class Position(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Structure(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Nation(models.Model):
    nation = models.CharField(max_length=100)
    def __str__(self):
        return self.nation