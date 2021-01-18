from django.contrib import admin
from .models import Category, Price, SkinType, Recommenditem


admin.site.register(Category)
admin.site.register(Price)
admin.site.register(SkinType)
admin.site.register(Recommenditem)