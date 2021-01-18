from rest_framework import generics
from cosme.models import Recommenditem
from cosme.api.permissions import IsAdminUserOrReadOnly
from cosme.api.serializers import RecommenditemSerializeras


class ListView(generics.ListCreateAPIView):
    queryset = Recommenditem.objects.all()
    serializer_class = RecommenditemSerializeras
    permission_classes = [IsAdminUserOrReadOnly]


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommenditem.objects.all()
    serializer_class = RecommenditemSerializeras
    permission_classes = [IsAdminUserOrReadOnly]