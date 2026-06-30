from django.shortcuts import render, redirect
from products.models import Product,Category,Color
from reviews.models import Review
from django.shortcuts import get_object_or_404
from accounts.models import CustomerProfile
from reviews.models import Review
from reviews.forms import ReviewForm
from django.contrib import messages
from carts.models import Cart, CartItem
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def product_list(request):
    products = Product.objects.all()
    search = request.GET.get("search")
    exclusive_products = Product.objects.filter(reviews__isnull=False).distinct()
    all_reviews = Review.objects.all()
    category_slug = request.GET.get('category',None)
    countCartItems = CartItem.objects.filter(cart__customer__user=request.user).count()
    if search:
        products = products.filter(
            Q(product_name__icontains=search)            |
            Q(slug__icontains=search)                    |
            Q(description__icontains=search)             |
            Q(category__category_name__icontains=search) | 
            Q(tags__name__icontains=search)              | 
            Q(warranty__icontains=search)                |
            Q(guarantee__icontains=search)
        ).distinct()
    if category_slug:
        current_category = Category.objects.filter(
            slug = category_slug
        ).first()

        products = Product.objects.filter(
            category = current_category
        )
    categories = Category.objects.all()
    return render(
        request=request,
        template_name='products/product_category.html',
        context={
            'products': products,
            'categories': categories,
            'current_category': category_slug,
            'exclusive_products': exclusive_products,
            'all_reviews': all_reviews,
            'cart_items' : countCartItems,
        }
    )

@login_required
def product_detail_view(request, pk):
    product = Product.objects.filter(id=pk).first()
    customer = get_object_or_404(CustomerProfile, user=request.user)
    color=Color.objects.filter().first()
    relatedProduct = Product.objects.filter(category=product.category)
    countCartItems = CartItem.objects.filter(cart__customer__user=request.user).count()
    cart, _ = Cart.objects.get_or_create(customer=customer)
    items = cart.cart_items.filter(variant__product=product).first()
    itemQuan = items.quantity if items else 0
    reviewTrueOrFalse = False
    if Review.objects.filter(customer=customer, product=product).exists():
        reviewTrueOrFalse = True
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.customer = customer
            review.product = product
            review.save()
            messages.success(request, 'Review submitted.')
            return redirect('product_detail', pk=product.id)
    else:
        form = ReviewForm()
    if product:
        return render(
            request=request,
            template_name='products/product_detail.html',
            context={
                'product': product,
                'color' : color,
                'review': reviewTrueOrFalse, 
                'form': form,
                'related_products': relatedProduct,
                'cart_items' : countCartItems,
                "stock": product.product_variants.first().stock,
                "item_quan": itemQuan,
            }
        )
    else:
        return render(
            request=request,
            template_name='products/product_detail.html',
            context={
                'message': "Product detail not found!",

            }
        )

@login_required
def cart_detailForMenu(request):
    customer = get_object_or_404(CustomerProfile,user=request.user)
    cart,_ = Cart.objects.get_or_create(customer = customer)
    items = cart.cart_items.filter(quantity__gt=0)
    total_price = 0
    for item in items:
        total_price += item.subtotal
    return render(
        request=request,
        template_name='products/product_detail.html',
        context={
            'cart':cart,
            'items':items,
            'total_price':total_price
        }
    )

@login_required
def pageNotFound(request):
    return render(request=request, template_name='error/404page.html')