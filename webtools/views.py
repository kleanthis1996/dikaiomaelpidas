# Django
from django.views.generic import TemplateView
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