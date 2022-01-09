from product.models import Category, Product, Images
from django.contrib import admin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from django.utils.html import format_html

class ProductImageınline(admin.TabularInline):
  model = Images
  extra = 5
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title', 'status',]
  list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
  list_display = ['title' ,'category' ,'price' ,'amount','image_tag' ,'status']
  list_filter = ['status', 'category']
  inlines = [ProductImageınline]
  readonly_fields = ('image_tag',)


class ImageAdmin(admin.ModelAdmin):
  list_display = ['title', 'product', 'image_tag']
  readonly_fields = ('image_tag',)
  
class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
  list_display = ('tree_actions', 'something',)
  list_display_links = ('something',)
  
  def something(self, instance):
    return format_html(
      '<div style="text-indent:{}px">{}</div>',
      instance._mpttfield('level') * self.mptt_level_indent,
      instance.title,
    )
  something.short_description = 'Category'

admin.site.register(Category, MyDraggableMPTTAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images, ImageAdmin)
