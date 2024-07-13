from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import StudentViewSet, ContentCreatorViewSet, AdminViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='students')
router.register('contentcreators', ContentCreatorViewSet, basename='contentcreators')
router.register('admins', AdminViewSet, basename='admins')

urlpatterns = [
    path('', include(router.urls))
]