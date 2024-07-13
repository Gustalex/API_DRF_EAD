from rest_framework.viewsets import ModelViewSet

from .models import Student, ContentCreator, Admin
from .serializers import StudentSerializer, ContentCreatorSerializer, AdminSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ContentCreatorViewSet(ModelViewSet):
    queryset = ContentCreator.objects.all()
    serializer_class = ContentCreatorSerializer

class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

