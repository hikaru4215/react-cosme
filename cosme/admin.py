from django.contrib import admin
from .models import Category, Price, SkinType, Score, Recommenditem, Review


admin.site.register(Category)
admin.site.register(Price)
admin.site.register(SkinType)
admin.site.register(Score)
admin.site.register(Recommenditem)
admin.site.register(Review)