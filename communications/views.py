from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
# from django.core.urlresolvers import reverse

from .models import Communication
from .forms import CommunicationForm


@login_required
def comm_details(request, uuid):

    comm = Communication.objects.get(uuid=uuid)
    if comm.owner != request.user:
            return HttpResponseForbidden()

    return render(request, 'communications/comm_detail.html', {'comm': comm})


@login_required()
def comm_cru(request):

    if request.POST:
        form = CommunicationForm(request.POST)
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
        form = CommunicationForm()

    template_vars = {
        'form': form,
    }

    template_name = 'communications/comm_creation.html'

    return render(request, template_name, template_vars)
