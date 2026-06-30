import stripe

from django.conf import settings
from django.core.management.base import BaseCommand
import os
from products.models import Product
from dotenv import load_dotenv
load_dotenv() 

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")


class Command(BaseCommand):
    help = "Create Stripe Products & Prices"

    def handle(self, *args, **kwargs):

        products = Product.objects.select_related("category").all()

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"Found {products.count()} products"))
        self.stdout.write("")

        for product in products:

            # Skip if already synced
            if product.stripe_product_id and product.stripe_price_id:
                self.stdout.write(
                    self.style.WARNING(
                        f"Skipped: {product.product_name}"
                    )
                )
                continue

            try:

                stripe_product = stripe.Product.create(
                    name=product.product_name,
                    description=product.description,
                    metadata={
                        "slug": product.slug,
                        "category": product.category.slug,
                        "product_id": product.id,
                    },
                )

                stripe_price = stripe.Price.create(
                    product=stripe_product.id,
                    unit_amount=int(product.price * 100),
                    currency="usd",
                )

                product.stripe_product_id = stripe_product.id
                product.stripe_price_id = stripe_price.id

                product.save(
                    update_fields=[
                        "stripe_product_id",
                        "stripe_price_id",
                    ]
                )

                self.stdout.write(
                    self.style.SUCCESS(
                        f"✔ {product.product_name}"
                    )
                )

            except Exception as e:

                self.stdout.write(
                    self.style.ERROR(
                        f"✘ {product.product_name}"
                    )
                )

                self.stdout.write(str(e))

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS("Stripe seed completed.")
        )