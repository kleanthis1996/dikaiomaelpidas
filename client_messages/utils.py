from client_messages.models import ContactUsMessage


def client_messages_badge_callback(request):
    pending_client_messages = ContactUsMessage.objects.filter(status=ContactUsMessage.STATUS_PENDING).count()
    return pending_client_messages