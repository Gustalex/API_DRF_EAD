from django.db import models

from User.models import Student
from Course.models import Course


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student.first_name + ' ' + self.student.last_name + ' - ' + self.student.cpf + ' - ' + self.course.name

    