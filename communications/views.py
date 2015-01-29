from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
# from django.core.urlresolvers import reverse

from .models import Communication
from .forms import CommunicationForm
from accounts.models import Account


@login_required
def comm_details(request, uuid):

    comm = Communication.objects.get(uuid=uuid)
    if comm.owner != request.user:
            return HttpResponseForbidden()

    return render(request, 'communications/comm_detail.html', {'comm': comm})


@login_required
def comm_creation(request, uuid=None, account=None):

    if uuid:
        comm = get_object_or_404(Communication, uuid=uuid)
        if comm.owner != request.user:
            return HttpResponseForbidden()
    else:
        comm = Communication(owner=request.user)

    if request.POST:
        form = CommunicationForm(request.POST, instance=comm)

        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']

            if account.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            comm = form.save(commit=False)
            comm.owner = request.user
            comm.save()
            # return the user to the account detail view
            reverse_url = reverse('account_detail', args=(account.uuid,))
            return redirect(reverse_url)
        else:
            account = form.cleaned_data['account']

    else:
        form = CommunicationForm(instance=comm)
    acc_id = request.GET.get('account', '')

    if acc_id:
        account = Account.objects.get(id=acc_id)

    template_vars = {
        'form': form,
        'comm': comm,
        'account': account
    }

    template_name = 'communications/comm_creation.html'

    return render(request, template_name, template_vars)
