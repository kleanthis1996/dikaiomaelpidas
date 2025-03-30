# Django
import datetime
import os

from django.conf import settings
from django.core.files import File
from django.http import JsonResponse
from django.views.generic import TemplateView

from news_and_events.models import Post, PostCategory, PostVariation
from programs.models import Program, ProgramCategory
from team_members.models import Member, JobRole, MemberCategory
from translations.models import Slug, Translation, Language
# Local
from webtools.models import Documentation, Announcement, StatusAbstract
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


def get_latest_active_announcement(request):
    """
    API used to fetch latest active announcements.
    :param request:
    :return:
    """
    result = {}
    latest_active_announcement = Announcement.objects.filter(status=True).order_by("-created_at").first()
    if latest_active_announcement:
        result = {
            "id": latest_active_announcement.id,
            "image_name": f"/mediafiles/{latest_active_announcement.image}"
        }
    return JsonResponse(result, safe=False)
