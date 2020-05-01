from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from contacts.models import Contact

def login(request):
    if request.method == 'POST':
        # Login user
        # Get form values
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Your username or password is not correct.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')


def registration(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken.')
                return redirect('registration')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'That email is being used.')
                return redirect('registration')
            else:
                # Create user
                user = User.objects.create_user(
                    username=username, email=email, password=password, first_name=first_name, last_name=last_name)

                # Login after register
                # auth.login(request, user)
                # messages.success(request, 'You are now logged in.')
                # return redirect('index')

                user.save()
                messages.success(request, 'Yeah! You\'re successsfully registered.')
                return redirect('login')

        else:
            messages.error(request, 'Passwords do not match.')
            return redirect('registration')

    else:
        return render(request, 'accounts/registration.html')


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

        context = {
            'contacts': contacts
        }
        
        return render(request, 'accounts/dashboard.html', context)
