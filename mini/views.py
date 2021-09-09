from .models import Mini
from  rest_framework import viewsets, permissions
from .serializers import MiniSerializer

# Create your views here.
class MiniViewSet(viewsets.ModelViewSet):
    queryset = Mini.objects.all()
    serializer_class = MiniSerializer
    permission_class = [permissions.AllowAny]