from django.shortcuts import redirect

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request URL is for the CMS section or client_messages URLs
        if request.path.startswith('/admin/') or request.path.startswith('/client_messages/') or request.path.startswith('/webtools/') or request.path.startswith('/ckeditor5/') or request.path.startswith('/mediafiles/'):
            return self.get_response(request)  # Skip language handling for CMS URLs
        path_parts = request.path.strip("/").split("/")
        valid_languages = ["en", "el"]  # Define supported languages

        if path_parts and path_parts[0] in valid_languages:
            lang = path_parts[0]  # Valid language found in URL
        else:
            lang = "en"  # Default to English
            return redirect(f"/{lang}/" + "/".join(path_parts[1:]))  # Properly replace language

        request.session.setdefault("language", lang)  # Store in session
        request.language = lang  # Attach to request object
        request.available_languages = [("en", "English"), ("el", "Greek")]

        return self.get_response(request)