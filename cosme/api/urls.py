from django.urls import path
from cosme.api import views

urlpatterns = [
    path("cosme/", views.ListView.as_view(), name="list"),
    path("cosme/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("review/", views.ReviewView.as_view(), name="review"),
]