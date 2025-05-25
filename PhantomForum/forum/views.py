from django.views.generic import TemplateView, DetailView, CreateView, ListView
from .models import Request, Commentary
from .forms import AddRequest, AddCommentary

# Create your views here.
class AboutView(TemplateView):
    template_name = "forum/about.html"

class RequestView(DetailView):
    model = Request
    template_name = "forum/request_view.html"

class ListRequestsView(ListView):
    template_name = "forum/list_requests.html"
    context_object_name = "requests"

    def get_queryset(self):
        return Request.objects.all()

class ListCommentariesView(ListView):
    template_name = "forum/commentary.html"
    context_object_name = "commentaries"

    def get_queryset(self):
        return Commentary.objects.all()

class AddRequestView(CreateView):
    template_name = "forum/add_request.html"
    model = Request
    form_class = AddRequest

    success_url = '/'

class AddCommentaryView(CreateView):
    model = Commentary
    template_name = "forum/add_commentary.html"
    form_class = AddCommentary
    success_url = "/commentary"


