# django
from django.urls import path
# local
from . import views

app_name = "webtools"

urlpatterns = [
    path("api/create-mock-data", views.create_mock_data, name="api-create-mock-data"),
]
