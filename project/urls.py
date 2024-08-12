from django.urls import path
from .views import AdsView, ContactView, TagView, CategoryView, ProductView, SubCategoryView, SocialLinksView, \
    ProductDetailView

urlpatterns = [
    path('', ProductView.as_view(), name='product-list'),
    path('<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('ads/', AdsView.as_view(), name='ads-list'),
    path('contact/', ContactView.as_view(), name='contact-list'),
    path('tag/', TagView.as_view(), name='tag-list'),
    path('category/', CategoryView.as_view(), name='category-list'),
    path('subcategory/', SubCategoryView.as_view(), name='subcategory-list'),
    path('socialLinks/', SocialLinksView.as_view(), name='socialList')
]
