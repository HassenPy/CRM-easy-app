from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Subscriber
from .forms import SubscriberForm


def subscriber_view(request, template_name='subscribers/signup_template.html'):

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():

            #Creating the User record
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()

            #Creating the Subscriber record
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']

            sub = Subscriber(address_one=address_one, address_two=address_two,
                             state=state, city=city,
                             user_rec=user)
            sub.save()
            print 'saved'
            return redirect('/success/')

    else:
        form = SubscriberForm()
    return render(request, template_name, {'form': form})
