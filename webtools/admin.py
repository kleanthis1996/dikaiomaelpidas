# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.urls import path, reverse_lazy
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# local
from webtools.models import ContactInformation, Documentation, Announcement
from webtools.views import DocumentationDetailView
# third party
from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass


@admin.register(ContactInformation)
class ContactInformationAdmin(ModelAdmin):
    list_display = ("id", "category", "type", "value")
    list_filter = ("category",)


@admin.register(Documentation)
class DocumentationAdmin(ModelAdmin):
    list_display = ("id", "title", "get_documentation_detail_url")

    def get_urls(self):
        documentation_detail_view = self.admin_site.admin_view(DocumentationDetailView.as_view(model_admin=self))
        return super().get_urls() + [
            path(
                "documentation-detail/<int:doc_id>", documentation_detail_view, name="documentation_detail"
            ),
        ]

    def get_documentation_detail_url(self, obj):
        documentation_url = reverse_lazy("admin:documentation_detail", kwargs={"doc_id": obj.pk})
        return format_html(f'<a href="{documentation_url}" target="_blank">View</a>')

    get_documentation_detail_url.short_description = "Documentation Detail"

    def has_add_permission(self, request):
        return request.user.is_superuser  # Only superusers can add

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser  # Only superusers can edit


@admin.register(Announcement)
class AnnouncementAdmin(ModelAdmin):
    list_display = ("id", "title", "get_image", "status", "created_at")

    def get_image(self, obj):
        return mark_safe(f'<img src="/mediafiles/{obj.image}" width="50" height="30" />')
    get_image.short_description = "Image"