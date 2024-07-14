from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    course_title = serializers.SerializerMethodField()
    
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'student_name', 'course', 'course_title', 'status', 'created_at', 'updated_at']
    
    
    def get_student_name(self, obj):
        return obj.student.first_name + ' ' + obj.student.last_name
    
    def get_course_title(self, obj):
        return obj.course.title
        
