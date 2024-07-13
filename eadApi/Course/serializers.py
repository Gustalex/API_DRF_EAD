from rest_framework import serializers
from .models import Course, CourseCategory

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseCategory
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    
    class Meta:
        model=Course
        fields=['id', 'title', 'description', 'duration', 'category', 'category_name']
    
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None