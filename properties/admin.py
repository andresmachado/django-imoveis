from django.contrib import admin

from .models import Property, Category, PropertyType


admin.site.register(Category)
admin.site.register(PropertyType)
admin.site.register(Property)
