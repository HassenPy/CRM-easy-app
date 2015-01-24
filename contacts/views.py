from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from .models import Contact
from .form import ContactForm


@login_required
def contact_detail(request, uuid):
    contact = Contact.objects.get(uuid=uuid)
    return render(request,
                  'contacts/contact_detail.html',
                  {'contacts': contact}
                  )


@login_required
def cont_creation(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            account = form.cleaned_data['account']

            if account.owner != request.user:
                return HttpResponseForbidden

            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()

            reverse_url = reverse('account_detail', args=(account.uuid,))
            print 'hi'
            return redirect(reverse_url)
    else:
        form = ContactForm()

    template_vars = {'form': form}
    template = 'contacts/contact_creation.html'
    return render(request, template, template_vars)
