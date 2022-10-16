from django.views.generic import TemplateView
# from mypolls.models import About


class IndexView(TemplateView):
    template_name = 'config/index.html'

    def get_context_data(self):
        context = super(IndexView, self).get_context_data()
        context["home"] = "I am here"
        return context


class AboutView(TemplateView):
    template_name = 'config/about.html'

    def get_context_data(self):
        context = super(AboutView, self).get_context_data()
        # context["about"] = About.objects.filter(name='ashu')
        return context

