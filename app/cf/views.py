from django.views.generic import TemplateView


class GetIPAddress(TemplateView):
    template_name = 'index.html'