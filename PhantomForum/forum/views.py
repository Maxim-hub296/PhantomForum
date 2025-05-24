from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, CreateView
from .models import Request
from .forms import AddRequest
from django.urls import reverse_lazy

# Create your views here.
class AboutView(TemplateView):
    template_name = "forum/about.html"

class RequestView(DetailView):
    model = Request
    template_name = "forum/request_view.html"

class AddRequestView(CreateView):
    template_name = "forum/add_request.html"
    model = Request
    form_class = AddRequest

    success_url = '/'


