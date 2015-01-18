from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms.forms import NON_FIELD_ERRORS
from django.conf import settings
from django.core.urlresolvers import reverse

from .models import Subscriber
from .forms import SubscriberForm

import stripe


def subscriber_view(request, template_name='subscribers/signup_template.html'):

    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        if form.is_valid():

            # Creating the User record
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User(username=username, email=email,
                        first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()

            # Creating the Subscriber record
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']

            sub = Subscriber(address_one=address_one, address_two=address_two,
                             state=state, city=city,
                             user_rec=user)
            sub.save()

            fee = settings.SUBSCRIPTION_PRICE
            try:
                sub.charge(request, email, fee)
                print 'yo ****************'
            except stripe.StripeError as e:
                form._errors[NON_FIELD_ERRORS] = form.error_class([e.args[0]])

                return render(request, template_name,
                              {'form': form,
                               'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
                               })

            a_u = authenticate(username=username, password=password)
            if a_u is not None:
                if a_u.is_active:
                    login(request, a_u)
                    return redirect(reverse('account_list'))
                else:
                    return redirect(reverse('django.contrib.auth.views.login'))
            else:
                return redirect(reverse('signup_url'))

    else:
        form = SubscriberForm()

    return render(request, template_name,
                  {'form': form,
                   'STRIPE_PUBLISHABLE_KEY': settings.STRIPE_PUBLISHABLE_KEY
                   })
