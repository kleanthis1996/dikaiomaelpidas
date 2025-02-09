from django.http import JsonResponse
from django.shortcuts import render

from client_messages.functions import get_user_input_contact_us_form
from client_messages.models import ContactUsMessage


def submit_contact_us_message(request):
    """
    view used to submit contact us message. To be used with AJAX call
    :param request:
    :return:
    """
    result = {"message": ""}
    try:
        # Accept only POST request, in other request methods, raise method not allowed
        if request.method == "POST":
            # Get input from user
            first_name, last_name, email, message = get_user_input_contact_us_form(
                request)
            # Create contact us message
            ContactUsMessage.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                message=message
            )
            result["message"] = "Contact us message submitted successfully"
            response_status = 200
        else:
            result["message"] = "Method not allowed"
            response_status = 405
    except Exception as error:
        print(error)
        response_status = 400
        result["message"] = "Something went wrong while submitting the contact us message"
    return JsonResponse({"message": result}, status=response_status)