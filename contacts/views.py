from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Contact
from .form import ContactForm
from accounts.models import Account


@login_required
def contact_detail(request, uuid):
    contact = Contact.objects.get(uuid=uuid)
    return render(request,
                  'contacts/contact_detail.html',
                  {'contacts': contact}
                  )


@login_required
def cont_creation(request, uuid=None, account=None):

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

            reverse_url = reverse('account_detail', args=(account.uuid,))
            return redirect(reverse_url)
        else:
            account = form.cleaned_data['account']
    else:
        form = ContactForm(instance=Contact)

    if request.GET.get('account', ''):
        account = Account.objects.get(id=request.GET.get('account', ''))

    template_vars = {'form': form,
                     'contact': contact,
                     'account': account
                     }

    template = 'contacts/contact_creation.html'
    return render(request, template, template_vars)
