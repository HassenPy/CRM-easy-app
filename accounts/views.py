from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from .models import Account
from .forms import AccountForm

import time


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


@login_required
def account_detail(request, uuid):
    print 'why here !'
    account = Account.objects.get(uuid=uuid)
    if account.owner != request.user:
        return HttpResponseForbidden()
    return render(request, 'accounts/account_details.html', {'account': account})


@login_required
def acc_creation(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            to_add = form.save(commit=False)
            to_add.owner = request.user
            to_add.save()
            time.sleep(0.05)
            print 'already here'
            redirect_url = reverse('account_detail',
                                   args=(to_add.uuid,))
            return redirect(redirect_url)

    else:
        form = AccountForm()
    return render(request, 'accounts/account_creation.html', {'form': form})
