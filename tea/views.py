from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tea
from django.db.models import Q
# Create your views here.


class TeaListView(ListView):
    """
    View for listing the compositions - uses build in ListView
    """
    model = Tea
    template_name = "index.html"
    ordering = ['name']

    def get_queryset(self):
        if self.request.GET.get("search", None):
            search = self.request.GET["search"]
            name_query = Q(name__contains=search)
            ing_query = Q(ingredients__name__contains=search)
            return Tea.objects.filter(name_query | ing_query).distinct()
        else:
            return Tea.objects.all().order_by("name")


class TeaDetailView(DetailView):
    """
    View for listing the compositions - uses build in ListView
    """
    model = Tea
    template_name = "detail.html"
