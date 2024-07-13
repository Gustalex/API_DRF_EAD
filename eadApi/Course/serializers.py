from rest_framework import serializers
from .models import Course, CourseCategory

class CourseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseCategory
        fields='__all__'

class CourseSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    creator_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'duration', 'category', 'category_name', 'creator', 'creator_name']
    
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None
    
    def get_creator_name(self, obj):
        if obj.creator:
            return obj.creator.first_name + ' ' + obj.creator.last_name
        return None
