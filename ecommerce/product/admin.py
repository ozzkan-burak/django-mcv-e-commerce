from product.models import Category
from django.contrib import admin

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title', 'status']
  list_filter = ['status']

admin.site.register(Category, CategoryAdmin)
