from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from datetime import date

from products.models import Product
from users.forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            dob = form.cleaned_data.get('date_of_birth')
            if dob is None:
                messages.error(request, "Date of birth is required.")
                return render(request, 'users/register.html', {'form': form})

            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            if age < 21:
                messages.error(request, "You must be at least 21 years old to register.")
                return render(request, 'users/register.html', {'form': form})

            # ✅ Save user (date_of_birth is not part of User, so skipped)
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            dob = getattr(user, 'date_of_birth', None)
            if dob:
                today = date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if age < 21:
                    messages.error(request, "You must be at least 21 years old to log in.")
                    return redirect('login')

            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def buyer_dashboard(request):
    products = Product.objects.all()  # or filter based on some buyer preferences
    return render(request, 'users/dashboard.html',{
        'users': request.user,
        'products': products
})




