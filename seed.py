#!/usr/bin/env python
"""
Run with: python seed.py
Seeds Category, Product, and ProductVariant data.
Skips entries that already exist (idempotent).
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from products.models import Category, Product, ProductVariant

CATEGORIES = [
    {'category_name': 'Electronics', 'slug': 'electronics'},
    {'category_name': 'Clothing', 'slug': 'clothing'},
    {'category_name': 'Books', 'slug': 'books'},
    {'category_name': 'Home & Garden', 'slug': 'home-garden'},
    {'category_name': 'Sports', 'slug': 'sports'},
    {'category_name': 'Chairs', 'slug': 'chairs'},
    {'category_name': 'Sofas', 'slug': 'sofas'},
    {'category_name': 'Tables', 'slug': 'tables'},
]
PRODUCTS = [
    {
        'product_name': 'Enim Expedita Sed',
        'category_slug': 'chairs',
        'slug': 'wooden-bar-stool',
        'description': 'Minimalist wooden bar stool crafted from solid oak with footrest support.',
        'price': '45.00',
        'variants': [
            {'color': 'Natural Oak', 'stock': 25},
            {'color': 'Ash White', 'stock': 15},
        ],
    },
    {
        'product_name': 'Adipisci Officia Libero',
        'category_slug': 'chairs',
        'slug': 'modern-black-bar-chair',
        'description': 'Contemporary black shell bar chair with wooden legs and metal footrest.',
        'price': '55.00',
        'variants': [
            {'color': 'Black', 'stock': 20},
            {'color': 'Dark Grey', 'stock': 10},
        ],
    },
    {
        'product_name': 'Internet Tend To Repeat',
        'category_slug': 'chairs',
        'slug': 'lounge-shell-chair',
        'description': 'Premium lounge chair featuring molded wood shell and soft cushion.',
        'price': '68.00',
        'variants': [
            {'color': 'White Walnut', 'stock': 12},
            {'color': 'Cream Oak', 'stock': 8},
        ],
    },
    {
        'product_name': 'Many Desktop Publishing',
        'category_slug': 'chairs',
        'slug': 'orange-bar-chair',
        'description': 'Stylish bar chair with molded seat and powder-coated steel frame.',
        'price': '69.00',
        'variants': [
            {'color': 'Orange', 'stock': 18},
            {'color': 'Red', 'stock': 14},
        ],
    },
    {
        'product_name': 'Injected Humour',
        'category_slug': 'chairs',
        'slug': 'classic-dining-chair',
        'description': 'Elegant walnut dining chair inspired by Scandinavian furniture design.',
        'price': '45.00',
        'variants': [
            {'color': 'Walnut', 'stock': 30},
            {'color': 'Teak', 'stock': 12},
        ],
    },
    {
        'product_name': 'Randomised Humour',
        'category_slug': 'chairs',
        'slug': 'designer-bird-chair',
        'description': 'Decorative designer chair with artistic bird-inspired aesthetics.',
        'price': '55.00',
        'variants': [
            {'color': 'Brown', 'stock': 10},
            {'color': 'Black', 'stock': 10},
        ],
    },
    {
        'product_name': 'Expedita Distinctio Rerum',
        'category_slug': 'chairs',
        'slug': 'fabric-arm-chair',
        'description': 'Comfortable upholstered armchair suitable for living rooms and lounges.',
        'price': '68.00',
        'variants': [
            {'color': 'Sky Blue', 'stock': 15},
            {'color': 'Light Grey', 'stock': 12},
        ],
    },
    {
        'product_name': 'Itaque Earum Rerum',
        'category_slug': 'chairs',
        'slug': 'wooden-arm-chair',
        'description': 'Natural wood armchair with padded seat and ergonomic design.',
        'price': '69.00',
        'variants': [
            {'color': 'Natural Wood', 'stock': 20},
            {'color': 'Oak White', 'stock': 8},
        ],
    },
    {
        'product_name': 'Consequuntur Magnam Dolores',
        'category_slug': 'chairs',
        'slug': 'velvet-accent-chair',
        'description': 'Luxury velvet accent chair designed for modern interiors.',
        'price': '89.00',
        'variants': [
            {'color': 'Emerald Green', 'stock': 10},
            {'color': 'Royal Blue', 'stock': 10},
        ],
    },
    {
        'product_name': 'Voluptatem Accusantium',
        'category_slug': 'chairs',
        'slug': 'mesh-office-chair',
        'description': 'Ergonomic office chair with breathable mesh back support.',
        'price': '95.00',
        'variants': [
            {'color': 'Black', 'stock': 25},
            {'color': 'Grey', 'stock': 15},
        ],
    },
    {
        'product_name': 'Tempora Quidem Harum',
        'category_slug': 'chairs',
        'slug': 'executive-leather-chair',
        'description': 'Executive leather office chair with adjustable recline and armrests.',
        'price': '129.00',
        'variants': [
            {'color': 'Black Leather', 'stock': 12},
            {'color': 'Brown Leather', 'stock': 8},
        ],
    },
    {
        'product_name': 'Repudiandae Culpa Nulla',
        'category_slug': 'chairs',
        'slug': 'rocking-chair',
        'description': 'Traditional wooden rocking chair for indoor relaxation.',
        'price': '79.00',
        'variants': [
            {'color': 'Walnut', 'stock': 10},
            {'color': 'Natural Oak', 'stock': 12},
        ],
    },
    {
        'product_name': 'Modern Fabric Sofa',
        'category_slug': 'sofas',
        'slug': 'modern-fabric-sofa',
        'description': 'Comfortable 3-seater fabric sofa with soft cushions and wooden legs.',
        'price': '299.00',
        'variants': [
            {'color': 'Grey', 'stock': 12},
            {'color': 'Beige', 'stock': 8},
        ],
    },
    {
        'product_name': 'Luxury Velvet Sofa',
        'category_slug': 'sofas',
        'slug': 'luxury-velvet-sofa',
        'description': 'Premium velvet sofa designed for modern living rooms.',
        'price': '449.00',
        'variants': [
            {'color': 'Emerald Green', 'stock': 6},
            {'color': 'Royal Blue', 'stock': 5},
        ],
    },
    {
        'product_name': 'Scandinavian Sofa',
        'category_slug': 'sofas',
        'slug': 'scandinavian-sofa',
        'description': 'Minimalist Scandinavian-style sofa with oak wood frame.',
        'price': '359.00',
        'variants': [
            {'color': 'Light Grey', 'stock': 10},
            {'color': 'Cream', 'stock': 7},
        ],
    },
    {
        'product_name': 'Leather Chesterfield Sofa',
        'category_slug': 'sofas',
        'slug': 'leather-chesterfield-sofa',
        'description': 'Classic Chesterfield sofa with premium leather upholstery.',
        'price': '599.00',
        'variants': [
            {'color': 'Brown', 'stock': 4},
            {'color': 'Black', 'stock': 6},
        ],
    },
    {
        'product_name': 'Corner Sectional Sofa',
        'category_slug': 'sofas',
        'slug': 'corner-sectional-sofa',
        'description': 'Large L-shaped sectional sofa perfect for family spaces.',
        'price': '799.00',
        'variants': [
            {'color': 'Dark Grey', 'stock': 5},
            {'color': 'Navy Blue', 'stock': 4},
        ],
    },
        {
        'product_name': 'Solid Oak Dining Table',
        'category_slug': 'tables',
        'slug': 'solid-oak-dining-table',
        'description': 'Elegant dining table crafted from premium solid oak wood.',
        'price': '349.00',
        'variants': [
            {'color': 'Natural Oak', 'stock': 10},
            {'color': 'Walnut', 'stock': 8},
        ],
    },
    {
        'product_name': 'Modern Coffee Table',
        'category_slug': 'tables',
        'slug': 'modern-coffee-table',
        'description': 'Minimalist coffee table with tempered glass top.',
        'price': '129.00',
        'variants': [
            {'color': 'Black', 'stock': 15},
            {'color': 'White', 'stock': 12},
        ],
    },
    {
        'product_name': 'Round Side Table',
        'category_slug': 'tables',
        'slug': 'round-side-table',
        'description': 'Compact side table suitable for bedrooms and living rooms.',
        'price': '79.00',
        'variants': [
            {'color': 'Oak', 'stock': 20},
            {'color': 'White', 'stock': 15},
        ],
    },
    {
        'product_name': 'Industrial Work Table',
        'category_slug': 'tables',
        'slug': 'industrial-work-table',
        'description': 'Industrial-style table with steel frame and wooden top.',
        'price': '219.00',
        'variants': [
            {'color': 'Rustic Brown', 'stock': 10},
            {'color': 'Dark Walnut', 'stock': 8},
        ],
    },
    {
        'product_name': 'Executive Office Desk',
        'category_slug': 'tables',
        'slug': 'executive-office-desk',
        'description': 'Spacious executive desk with cable management features.',
        'price': '399.00',
        'variants': [
            {'color': 'Mahogany', 'stock': 6},
            {'color': 'Black Oak', 'stock': 5},
        ],
    },
]

def seed():
    print("Seeding categories...")
    categories = {}
    for data in CATEGORIES:
        obj, created = Category.objects.get_or_create(
            slug=data['slug'],
            defaults={'category_name': data['category_name']},
        )
        categories[data['slug']] = obj
        print(f"  {'Created' if created else 'Exists '} → {obj.category_name}")

    print("\nSeeding products & variants...")
    for data in PRODUCTS:
        category = categories[data['category_slug']]
        product, created = Product.objects.get_or_create(
            slug=data['slug'],
            defaults={
                'product_name': data['product_name'],
                'category': category,
                'description': data['description'],
                'price': data['price'],
            },
        )
        print(f"  {'Created' if created else 'Exists '} → {product.product_name}")

        for v in data.get('variants', []):
            variant, v_created = ProductVariant.objects.get_or_create(
                product=product,
                color=v['color'],
                defaults={'stock': v['stock'], 'image': ''},
            )
            print(f"    {'Created' if v_created else 'Exists '} variant: {variant.color} (stock={variant.stock})")

    print("\nDone.")


if __name__ == '__main__':
    seed()