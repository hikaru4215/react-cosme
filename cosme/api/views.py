from rest_framework import generics, viewsets
from cosme.models import Recommenditem, Review
from cosme.api.permissions import IsAdminUserOrReadOnly
from cosme.api.serializers import RecommenditemSerializers, ReviewSerializers


class ListView(generics.ListCreateAPIView):
    queryset = Recommenditem.objects.all()
    serializer_class = RecommenditemSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommenditem.objects.all()
    serializer_class = RecommenditemSerializers
    permission_classes = [IsAdminUserOrReadOnly]


class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers
    permission_classes = [IsAdminUserOrReadOnly]