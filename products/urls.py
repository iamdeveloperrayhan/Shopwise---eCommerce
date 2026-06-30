from django.urls import path
from products import views
from shared.views import remove_cart_item

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('', views.cart_detailForMenu, name='cart_detailForMenu'),
    path('detail/<int:pk>/', views.product_detail_view, name='product_detail'),
    path("cart/remove/<int:pk>/", remove_cart_item, name="remove_cart_item"),
]
