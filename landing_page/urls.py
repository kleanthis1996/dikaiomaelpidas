# Django
from django.urls import path
# Local
from . import views

app_name = "landing_page"

urlpatterns = [
    path("<str:lang>/", views.index, name="index"),
    path("<str:lang>/about/", views.about, name="about"),
    path("<str:lang>/services/", views.services, name="services"),
    path("<str:lang>/events/", views.events, name="events"),
    path("<str:lang>/news/", views.news, name="news"),
    path("<str:lang>/contact/", views.contact, name="contact"),
    path("<str:lang>/support/", views.support, name="support"),
]
