from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from User.models import ContentCreator

class CourseCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'course_category'
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    creator = models.ForeignKey(ContentCreator, on_delete=models.CASCADE, related_name='course_creator')
    
    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return self.title

@receiver(post_save, sender=Course)
def update_content_creator_courses(sender, instance, created, **kwargs):
    if created:
        instance.creator.courses.add(instance)
