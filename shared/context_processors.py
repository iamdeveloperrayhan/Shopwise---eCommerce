from accounts.models import CustomerProfile
from carts.models import Cart, CartItem
from django.utils import timezone
from django.shortcuts import get_object_or_404
# Create your views here.
# context_processors.py

from django.shortcuts import get_object_or_404
from django.utils import timezone

def cart_data(request):
    if request.user.is_authenticated:
        customer = get_object_or_404(
            CustomerProfile,
            user=request.user
        )
        cart, _ = Cart.objects.get_or_create(customer=customer)
        items = cart.cart_items.filter(quantity__gt=0)
        for item in items:
            diff = timezone.now() - item.created_at
            seconds = int(diff.total_seconds())
            if seconds < 60:
                item.time_ago = f"{seconds}s ago"
            elif seconds < 3600:
                item.time_ago = f"{seconds // 60}m ago"
            elif seconds < 86400:
                item.time_ago = f"{seconds // 3600}h ago"
            else:
                item.time_ago = f"{seconds // 86400}d ago"

        total_price = sum(item.subtotal for item in items)
        return {
            'menu_cart': cart,
            'menu_items': items,
            'menu_total_price': total_price,
        }
    return {
        'menu_cart': None,
        'menu_items': [],
        'menu_total_price': 0,
    }