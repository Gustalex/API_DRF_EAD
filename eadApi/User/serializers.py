from rest_framework import serializers
from .models import Student, ContentCreator, Admin

class StudentSerializer(serializers.ModelSerializer):
    course_title = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'cpf', 'username', 'password', 'role', 'courses', 'course_title']
    
    def get_course_title(self, obj):
        return [course.title for course in obj.courses.all()]

    
class ContentCreatorSerializer(serializers.ModelSerializer):
    course_title = serializers.SerializerMethodField()
    class Meta:
        model = ContentCreator
        fields = ['id', 'first_name', 'last_name', 'email', 'cpf', 'username', 'password', 'role', 'courses', 'course_title']
    
    def get_course_title(self, obj):
        return [course.title for course in obj.courses.all()]
        
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'