from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse


def home_page(request, template_name='marketing/home.html'):
    """
    View to render the home page, nothing fancy
    """
    if request.user.is_authenticated():
        return redirect(reverse('account_list'))
    return render(request, template_name)
