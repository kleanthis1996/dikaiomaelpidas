# django
from django.urls import path
# local
from . import views

app_name = "webtools"

urlpatterns = [
    path("api/get-latest-active-announcement", views.get_latest_active_announcement,
         name="api-get-latest-active-announcement"),
]
