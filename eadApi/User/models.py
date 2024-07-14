from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    cpf = models.CharField(max_length=14, unique=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Student(User):
    courses = models.ManyToManyField('Course.Course', blank=True)
    role = models.CharField(max_length=50, default='student')
    class Meta:
        db_table = 'student'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

class Admin(User):
    role = models.CharField(max_length=50, default='admin')
    
    class Meta:
        db_table = 'admin'
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
    
class ContentCreator(User):
    courses = models.ManyToManyField('Course.Course', blank=True)
    role = models.CharField(max_length=50, default='content_creator')
    
    class Meta:
        db_table = 'content_creator'
        verbose_name = 'Content Creator'
        verbose_name_plural = 'Content Creators'
        