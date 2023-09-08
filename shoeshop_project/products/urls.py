from django.urls import path

from .views import *

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('shop/<slug:product_slug>', ShopView.as_view(), name='shop'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product-detail'),
    # path('contact/', contact, name='contact'),
    # path('collection/<slug:collection_name>/', CollectionView.as_view(), name='collection'),
    # path('category/<slug:category_name>/', CategoryView.as_view(), name='category'),
]