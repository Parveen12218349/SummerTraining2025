from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order, OrderItem
from django.utils import timezone

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        if quantity > 0 and quantity <= product.stock:
            # Create Order
            order = Order.objects.create(user=request.user, ordered_at=timezone.now())

            # Create OrderItem
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity
            )

            # Update product stock
            product.stock -= quantity
            product.save()

            return redirect('/products/dashboard/')  # Or redirect to a "Thank You" page
        else:
            error = "Invalid quantity selected."
            return render(request, 'orders/place_order.html', {
                'product': product,
                'error': error
            })

    return render(request, 'orders/place_order.html', {'product': product})
