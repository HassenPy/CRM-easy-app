from django.views.generic.base import TemplateView


class HomePage(TemplateView):
    """
    View to render the home page, nothing fancy
    """

    template_name = 'marketing/home.html'
