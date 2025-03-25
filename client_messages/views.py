# django
from django.http import JsonResponse
# local
from client_messages.functions import get_user_input_contact_us_form, get_user_input_volunteer_application
from client_messages.models import ContactUsMessage, VolunteerApplication, VolunteerSector
from translations.models import Slug, Translation


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


def submit_volunteer_application(request):
    """
    view used to submit volunteer application. To be used with AJAX call
    :param request:
    :return:
    """
    result = {"message": ""}
    try:
        # Accept only POST request, in other request methods, raise method not allowed
        if request.method == "POST":
            # Get user input from form
            (first_name, last_name, date_of_birth, home_address, phone_number,
             email, volunteer_sectors, experience_description, consent_given) = get_user_input_volunteer_application(
                request)

            # Create the volunteer application
            volunteer_application = VolunteerApplication.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                home_address=home_address,
                phone_number=phone_number,
                email=email,
                experience_description=experience_description,
                consent_given=consent_given
            )
            # Add the volunteer sectors which is a many to many field
            for volunteer_sector in volunteer_sectors:
                volunteer_sector_object = VolunteerSector.objects.filter(code=volunteer_sector).first()
                if volunteer_sector_object:
                    volunteer_application.volunteer_sectors.add(volunteer_sector_object)
                    continue
                # If other given, save it in db, without code, and is_other boolean to True
                # Create name of other volunter sector, translation, and finally the object
                volunteer_sector_name = Slug.objects.create(
                    description=f"{first_name} {last_name} other volunteer sector", )
                Translation.objects.create(
                    slug=volunteer_sector_name,
                    language_code=request.LANGUAGE_CODE,
                    text=f"{first_name} {last_name} {volunteer_sector}"
                )
                VolunteerSector.objects.create(
                    name=volunteer_sector_name,
                    is_other=True,
                )
            result["message"] = "Volunteer Application submitted successfully"
            response_status = 200
        else:
            result["message"] = "Method not allowed"
            response_status = 405
    except Exception as error:
        print(error)
        response_status = 400
        result["message"] = "Something went wrong while submitting the volunteer application"
    return JsonResponse({"message": result}, status=response_status)
