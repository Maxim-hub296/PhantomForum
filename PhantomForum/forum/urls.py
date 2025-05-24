from django.urls import path

from . import views

app_name = "forum"
urlpatterns = [
    path("", views.AboutView.as_view(), name="about"),
    path("create-target", views.AddRequestView.as_view(), name="create"),
    path("<int:pk>/", views.RequestView.as_view(), name="request"),
    path("targets/", views.ListRequestsView.as_view(), name='targets'),
]
