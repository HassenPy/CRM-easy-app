from django.shortcuts import render
# , redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


from .models import Account


class AccountList(ListView):
    model = Account
    paginate_by = 12
    template_name = "accounts/account_list.html"
    context_object_name = "accounts"

    def get_queryset(self):
        try:
            a = self.request.GET.get('account',)
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(name__icontains=a,
                                                  owner=self.request.user
                                                  )
        else:
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)
