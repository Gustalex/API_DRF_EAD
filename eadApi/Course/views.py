from rest_framework.viewsets import ModelViewSet

from .models import Course, CourseCategory
from .serializers import CourseSerializer, CourseCategorySerializer

class CourseCategoryViewSet(ModelViewSet):
    queryset = CourseCategory.objects.all()
    serializer_class = CourseCategorySerializer

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
