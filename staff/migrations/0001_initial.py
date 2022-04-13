# Generated by Django 3.2.5 on 2022-04-13 05:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Structure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(verbose_name='дата рождения')),
                ('nation', models.CharField(max_length=100)),
                ('iin', models.CharField(max_length=12)),
                ('adress', models.CharField(max_length=100, verbose_name='адрес')),
                ('photo', models.ImageField(upload_to='')),
                ('citizenship', models.CharField(max_length=100, verbose_name='гражаданство')),
                ('experience', models.CharField(max_length=100, verbose_name='стаж')),
                ('sex', models.CharField(choices=[('мужчина', 'мужчина'), ('женщина', 'женщина')], max_length=100, verbose_name='пол')),
                ('militaryID', models.BooleanField(default=True)),
                ('Type_of_education', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=100)),
                ('Couses', models.CharField(max_length=100)),
                ('speciality', models.CharField(max_length=100)),
                ('diploma', models.FileField(upload_to='')),
                ('fio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('postiton', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.position')),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.structure')),
            ],
        ),
    ]
