from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from carts.models import CartItem
# Create your views here.


def remove_cart_item(request, pk):
    if request.method == "POST":
        item = get_object_or_404(CartItem, pk=pk)
        item.delete()
        messages.success(request, "Item removed from cart")

    return redirect(request.META.get("HTTP_REFERER", "cart_detail"))