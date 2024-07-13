from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseCategoryViewSet, CourseViewSet

router = DefaultRouter()
router.register('categories', CourseCategoryViewSet, basename='category')
router.register('courses', CourseViewSet, basename='course')

urlpatterns = [
    path('', include(router.urls))
]

