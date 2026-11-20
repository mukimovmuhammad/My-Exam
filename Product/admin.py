from django.contrib import admin
from .models import Product


@admin.register(Product)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
    list_per_page = 5

