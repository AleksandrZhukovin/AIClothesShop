from django.views.generic import TemplateView


class CoverView(TemplateView):
    template_name = 'cover/index.html'
