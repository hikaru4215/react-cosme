from rest_framework import serializers
from cosme.models import Recommenditem

class RecommenditemSerializeras(serializers.ModelSerializer):
    class Meta:
        model = Recommenditem
        fields = "__all__"