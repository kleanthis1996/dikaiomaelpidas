# system
import re


def is_valid_email(email: str) -> bool:
    """
    Checks if the email is valid or not
    :param email:
    :return: True if the email is valid, False otherwise
    """
    # Define a regular expression pattern for a basic email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None


def get_user_input_contact_us_form(request) -> tuple or None:
    """
    Get and validate user email from POST request, for contact us form
    :param request:
    :return:
    """
    # Get user input from POST request
    first_name = request.POST["first-name"]
    last_name = request.POST["last-name"]
    email = request.POST["email"]
    message = request.POST["message"]

    # Validate user email
    if not is_valid_email(email):
        raise ValueError("Invalid email address")

    return first_name, last_name, email, message


def get_user_input_volunteer_application(request):
    """
    Get user input from POST request, for volunteer application form
    :param request:
    :return:
    """
    first_name = request.POST["first-name"]
    last_name = request.POST["last-name"]
    date_of_birth = request.POST["date-of-birth"]
    home_address = request.POST["home-address"]
    phone_number = request.POST["phone-number"]
    email = request.POST["email"]
    volunteer_sectors = request.POST["volunteer-sectors"]
    experience_description = request.POST["experience-description"]
    consent_given = request.POST["consent-given"]

    return first_name, last_name, date_of_birth, home_address, phone_number, email, volunteer_sectors, experience_description, consent_given
