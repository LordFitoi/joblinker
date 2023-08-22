from typing import Any, Dict
from django.views.generic import DetailView, ListView
from .models import Company, JobPost


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
    

class CompanyDetailView(ListView):
    template_name = "companies/company.html"
    model = JobPost
    paginate_by = 10


    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        
        return queryset.filter(company__slug=self.kwargs['company_slug'])
    
    def get_object(self):
        return Company.objects.filter(slug=self.kwargs['company_slug']).first()
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["company"] = self.get_object()

        return context

    