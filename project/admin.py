from django.contrib import admin
from .models import Ads, Tag, SocialLinks, Category, SubCategory, Contact, Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'created_at')
    list_display_links = ('id', 'title', 'price', 'created_at')
    list_filter = ('title',)
    filter_horizontal = ('tags',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')
    list_display_links = ('id', 'name', 'email', 'created_at')
    filter_horizontal = ('price',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Ads)
admin.site.register(Tag)
admin.site.register(SocialLinks)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category)
admin.site.register(SubCategory)
