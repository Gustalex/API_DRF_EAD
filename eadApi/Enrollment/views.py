from rest_framework.viewsets import ModelViewSet

from .models import Enrollment
from .serializers import EnrollmentSerializer

class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
