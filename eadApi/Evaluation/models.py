from django.db import models

from Course.models import Course
from User.models import Student

class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'evaluation'
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        unique_together = ('student', 'course')
    
    def __str__(self):
        return f'{self.student} - {self.course} - {self.grade}'
        
    
    