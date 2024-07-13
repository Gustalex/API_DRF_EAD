from django.db import models

class CourseCategory(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Course Category'
        verbose_name_plural = 'Course Categories'
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
    
    def __str__(self):
        return self.title
