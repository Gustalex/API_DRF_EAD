from rest_framework.viewsets import ModelViewSet


from .models import Evaluation
from .serializers import EvaluationSerializer

class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
