from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    sex = models.NullBooleanField()
    tel = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True)
    photo = models.ImageField(upload_to='media', null=True)
    title = models.CharField(max_length=20, null=True)
    academy = models.CharField(max_length=30, null=True)
    research = models.CharField(max_length=100, null=True)
    hobby = models.CharField(max_length=100, null=True)
    tag = models.NullBooleanField()
    password = models.CharField(max_length=50, null=True)


class Student(models.Model):
    name = models.CharField(max_length=20)
    tel = models.IntegerField()
    email = models.EmailField()
    education = models.CharField(max_length=20, null=True)
    academy = models.CharField(max_length=30, null=True)
    hobby = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=50, null=True)


class VIP(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class Appointment(models.Model):
    date = models.DateField()
    time = models.IntegerField()
    student = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20)
    student_email = models.EmailField()
    teacher_email = models.EmailField()
    topic = models.CharField(max_length=50, null=True)
    content = models.CharField(max_length=100, null=True)
    tag = models.IntegerField(default=-1)



