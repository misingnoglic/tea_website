from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Tea
# Create your views here.


def home(request):
    return render(request, "index.html")


class TeaListView(ListView):
    """
    View for listing the compositions - uses build in ListView
    """
    model = Tea
    template_name = "index.html"

class TeaDetailView(DetailView):
    """
    View for listing the compositions - uses build in ListView
    """
    model = Tea
    template_name = "detail.html"
