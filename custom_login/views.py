from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login


def custom_login(request, **kwargs):
    if request.user.is_authenticated():
        return redirect(reverse('home'))
    else:
        return login(request, template_name="login.html")
