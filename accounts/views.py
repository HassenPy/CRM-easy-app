# from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from .models import Account


class AccountList(ListView):
    model = Account
    template_name = "accounts/account_list.html"
    context_object_name = "accounts"

    def get_queryset(self):
        account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    @login_required
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)
