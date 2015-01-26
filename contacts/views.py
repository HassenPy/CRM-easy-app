from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic.edit import DeleteView

from .models import Contact
from .form import ContactForm
from accounts.models import Account


@login_required
def contact_detail(request, uuid):
    contact = Contact.objects.get(uuid=uuid)
    return render(request,
                  'contacts/contact_detail.html',
                  {'contact': contact}
                  )


@login_required
def cont_creation(request, uuid=None, account=None):
    print 'hi'
    if uuid:
        contact = get_object_or_404(Contact, uuid=uuid)
        if contact.owner != request.user:
            return HttpResponseForbidden
    else:
        contact = Contact(owner=request.user)

    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            account = form.cleaned_data['account']

            if account.owner != request.user:
                return HttpResponseForbidden

            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()

            # in case the request is ajax, we return the simple
            # form template instead of the whole page
            if request.is_ajax():
                return render(request,
                              'contacts/contact_item_view.html',
                              {'account': account, 'contact': contact}
                              )
            else:
                reverse_url = reverse('account_detail', args=(account.uuid,))
                return redirect(reverse_url)

        else:
            account = form.cleaned_data['account']

    else:
        form = ContactForm(instance=contact)

    if request.GET.get('account', ''):
        account = Account.objects.get(id=request.GET.get('account', ''))

    template_vars = {'form': form,
                     'contact': contact,
                     'account': account
                     }
    if request.is_ajax():
        template = 'contacts/contact_item_form.html'
    else:
        template = 'contacts/contact_creation.html'

    return render(request, template, template_vars)


class ContactMixin(object):
    model = Contact

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name': 'Contact'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactMixin, self).dispatch(*args, **kwargs)


class ContactDelete(ContactMixin, DeleteView):
    template_name = 'contacts/object_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(ContactDelete, self).get_object()
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
