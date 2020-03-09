from django.contrib import admin

from .models import Report, Category


admin.site.register(Category)
admin.site.register(Report)
