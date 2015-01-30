from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login


def home_page(request, template_name='marketing/home.html'):
    """
    View to render the home page, nothing fancy
    """
    if request.user.is_authenticated():
        return redirect(reverse('account_list'))
    return render(request, template_name)


def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    else:
        return login(request, template_name="login.html")
