# Django
from django.urls import path
# Local
from . import views

app_name = "landing_page"

urlpatterns = [
    path("<str:lang>/", views.index, name="index"),
    path("<str:lang>/about/", views.about, name="about"),
    path("<str:lang>/services/", views.services, name="services"),
    path("<str:lang>/events/<int:page>/", views.posts_list, name="events"),
    path("<str:lang>/event/<int:page>/", views.posts_detail, name="event_detail"),
    path("<str:lang>/news/<int:page>/", views.posts_list, name="news"),
    path("<str:lang>/new/<int:page>/", views.posts_detail, name="new_detail"),
    path("<str:lang>/contact/", views.contact, name="contact"),
    path("<str:lang>/support/", views.support, name="support"),
    path("<str:lang>/team/", views.team, name="team"),
]
