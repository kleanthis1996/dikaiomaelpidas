from client_messages.models import ContactUsMessage, VolunteerApplication


def client_messages_badge_callback(request):
    pending_client_messages = ContactUsMessage.objects.filter(status=ContactUsMessage.STATUS_PENDING).count()
    pending_volunteer_applications = VolunteerApplication.objects.filter(status=VolunteerApplication.STATUS_PENDING).count()
    return pending_client_messages + pending_volunteer_applications