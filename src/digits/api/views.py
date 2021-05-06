from rest_framework import viewsets

from digits.api.serializer import DigitSerializer
from ..models import Digit

class DigitViewSet(viewsets.ModelViewSet):
    serializer_class = DigitSerializer
    queryset = Digit.objects.all()
