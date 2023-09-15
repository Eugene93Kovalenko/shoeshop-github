from django.urls import path

# from orders.views import add_to_cart
from .views import *

app_name = 'products'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop/', ShopView.as_view(), name='shop'),
    path('product/<slug:product_slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('add_to_cart/<slug:product_slug>/', add_to_cart, name='add_to_cart'),
    # path('collection/<slug:collection_name>/', CollectionView.as_view(), name='collection'),
    # path('category/<slug:category_name>/', CategoryView.as_view(), name='category'),
]