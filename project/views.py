from rest_framework import generics
from .models import Ads, SubCategory, Category, Contact, Tag, SocialLinks, Product
from .serializer import AdsSerializer, ContactSerializer, CategorySerializer, TagSerializer, SubCategorySerializer, \
    ProductSerializer, SocialLinksSerializer


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class AdsView(generics.ListCreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer


class SubCategoryView(generics.ListCreateAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SocialLinksView(generics.ListCreateAPIView):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer


class ContactView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
