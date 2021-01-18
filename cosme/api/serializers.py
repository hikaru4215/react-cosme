from rest_framework import serializers
from cosme.models import Recommenditem, Review

class RecommenditemSerializers(serializers.ModelSerializer):
    class Meta:
        model = Recommenditem
        fields = "__all__"

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
        