# Django
from django.urls import path
# Local
from . import views

app_name = "landing_page"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("support/", views.support, name="support"),
    path("contact/", views.contact, name="contact"),
]