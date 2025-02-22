from functools import wraps

from webtools.models import ContactInformation


def get_contact_information(view_func):
    """
    Decorator used to load contact information in all HTML rendering views
    :param view_func:
    :return:
    """
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        # Get all contact information
        contact_information = ContactInformation.objects.all()
        # Parse a dict containing the details
        result = {
            ContactInformation.SOCIAL_CATEGORY:[],
            ContactInformation.CONTACT_CATEGORY: {}
        }
        for contact in contact_information:
            if contact.category == ContactInformation.CONTACT_CATEGORY:
                result[contact.category][contact.type] = contact.value
            elif contact.category == ContactInformation.SOCIAL_CATEGORY:
                result[contact.category].append({
                    'type': contact.type,
                    'value': contact.value
                })
        # Add in request
        request.contact_information = result
        return view_func(request, *args, **kwargs)
    return wrapped_view