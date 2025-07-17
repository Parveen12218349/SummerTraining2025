from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order, OrderItem

@login_required
def place_order(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        if 0 < quantity <= product.stock and address and payment_method:
            total_price = quantity * product.price

            order = Order.objects.create(
                buyer=request.user,
                total_amount=total_price,
                shipping_address=address,
                payment_method=payment_method
            )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price
            )

            product.stock -= quantity
            product.save()

            return redirect('/products/')
        else:
            error = "Please enter all required details and valid quantity."
            return render(request, 'orders/place_order.html', {
                'product': product,
                'error': error
            })

    return render(request, 'orders/place_order.html', {'product': product})
