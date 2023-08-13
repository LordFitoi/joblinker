from django.views.generic import DetailView
from .models import Company


class CompanyDetailView(DetailView):
    template_name = "companies/company.html"
    model = Company

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['company_slug'])