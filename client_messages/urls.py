# django
from django.urls import path
# local
from . import views

app_name = "client_messages"

urlpatterns = [
    path("api/submit-contact-us-messages", views.submit_contact_us_message, name="api-submit-contact-us-messages"),
    path("api/submit-volunteer-application", views.submit_volunteer_application, name="api-submit-volunteer-application"),
]
