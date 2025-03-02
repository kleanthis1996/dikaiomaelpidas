# Django
import os

from django.conf import settings
from django.core.files import File
from django.http import JsonResponse
from django.views.generic import TemplateView

from news_and_events.models import Post
from programs.models import Program
from team_members.models import Member, JobRole
from translations.models import Slug, Translation, Language
# Local
from webtools.models import Documentation
# Third Party
from unfold.views import UnfoldModelAdminViewMixin


class DocumentationDetailView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Documentation Detail"
    permission_required = ()
    template_name = "admin/documentation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get documentation id
        doc_id = kwargs.get("doc_id")
        # Get the documentation details
        documentation_detail = Documentation.objects.get(pk=doc_id)
        # Add custom context
        context["documentation_detail"] = documentation_detail
        return context

def create_mock_data(request):
    """
    API used to create mock data for dynamic parts.
    :param request:
    :return:
    """
    # Create Programs
    for i in range(0,9):
        # Create test slug for title
        test_title_slug = Slug.objects.create(
            description=f"Test Program Title {i}",
        )
        # Add English Translation
        Translation.objects.create(
            slug=test_title_slug,
            language=Language.objects.get(code="en"),
            text=f"Test Title Program {i}"
        )
        # Add Greek Translation
        Translation.objects.create(
            slug=test_title_slug,
            language=Language.objects.get(code="el"),
            text=f"Δοκιμαστικος Τιτλος Προγραμματος {i}"
        )
        # Create test slug for description
        test_description_slug = Slug.objects.create(
            description=f"Test Program Description {i}",
        )
        Translation.objects.create(
            slug=test_description_slug,
            language=Language.objects.get(code="en"),
            text=f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ut felis at lacus gravida varius. Integer at justo eget nisi fermentum luctus."
        )
        Translation.objects.create(
            slug=test_description_slug,
            language=Language.objects.get(code="el"),
            text="Αυτό είναι ένα δείγμα κειμένου για δοκιμή. Χρησιμοποιείται συνήθως για να ελέγξετε τη μορφοποίηση και τη διάταξη χωρίς πραγματικό περιεχόμενο."
        )

        # Path to the static image
        image_filename = "test_image_1.png" if i % 2 == 0 else "test_image_2.png"
        destination_path = os.path.relpath(f"mediafiles/test_images/{image_filename}")


        # Open the file
        with open(destination_path, "rb") as img_file:
            django_file = File(img_file)

            # Create the object
            Program.objects.create(
                name=test_title_slug,
                description=test_description_slug,
                image=django_file  # Assign the file to the image field
            )


    # Create Team Members
    destination_path = os.path.relpath(f"mediafiles/test_images/test_person.jpg")
    # Create 3 test roles and add 3 team members under each one
    for i in range(0,3):
        test_job_role_name = Slug.objects.create(
            description=f"Test Job Role {i}",
        )
        Translation.objects.create(
            slug=test_job_role_name,
            language=Language.objects.get(code="en"),
            text=f"Test Job Role {i}"
        )
        Translation.objects.create(
            slug=test_job_role_name,
            language=Language.objects.get(code="el"),
            text=f"Δοκιμαστικος ρολος {i}"
        )
        test_job_role=JobRole.objects.create(
            name=test_job_role_name,
        )

        for i in range(0,3):
            test_description_slug = Slug.objects.create(
                description=f"Test Member Description {i}",
            )
            Translation.objects.create(
                slug=test_description_slug,
                language=Language.objects.get(code="en"),
                text=f"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum ut felis at lacus gravida varius. Integer at justo eget nisi fermentum luctus."
            )
            Translation.objects.create(
                slug=test_description_slug,
                language=Language.objects.get(code="el"),
                text="Αυτό είναι ένα δείγμα κειμένου για δοκιμή. Χρησιμοποιείται συνήθως για να ελέγξετε τη μορφοποίηση και τη διάταξη χωρίς πραγματικό περιεχόμενο."
            )
            with open(destination_path, "rb") as img_file:
                django_file = File(img_file)
                Member.objects.create(
                    job_role=test_job_role,
                    full_name=f"Test Name",
                    profile_image=django_file,
                    description=test_description_slug,
                )

    # Create Events
    for i in range(0,36):
        Post.objects.create(

        )

    # Create News
    return JsonResponse({"message": "Success"})