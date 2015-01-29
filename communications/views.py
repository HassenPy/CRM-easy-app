from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, Http404
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse
# from django.core.urlresolvers import reverse

from .forms import CommunicationForm
from accounts.models import Account
from .models import Communication


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
            if request.is_ajax():
                return render(request,
                              'communications/comm_item_view.html',
                              {'comm': comm, 'account': account}
                              )

            # return the user to the account detail view
            else:
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
    if request.is_ajax():
        template_name = 'communications/comm_item_form.html'
    else:
        template_name = 'communications/comm_creation.html'

    return render(request, template_name, template_vars)


class CommMixin(object):
    model = Communication

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Communication'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CommMixin, self).dispatch(*args, **kwargs)


class CommDelete(CommMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(CommDelete, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        account = Account.objects.get(id=obj.account.id)
        self.account = account
        return obj

    def get_success_url(self):
        return reverse(
            'account_detail',
            args=(self.account.uuid,)
        )
