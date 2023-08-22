from django.views.generic import DetailView, ListView
from .models import Company, JobPost


class CompanyDetailView(DetailView):
    template_name = "companies/company.html"
    model = Company

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['company_slug'])


class JobpostListView(ListView):
    template_name="index.html"
    model = JobPost
    paginate_by = 10


    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        return queryset
    

class CompanyListView(ListView):
    template_name="companies/index.html"
    model = Company
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        return queryset
    


    