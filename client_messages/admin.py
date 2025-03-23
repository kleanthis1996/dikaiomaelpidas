# django
from django.contrib import admin
# local
from client_messages.models import ContactUsMessage, VolunteerApplication, VolunteerSector
# third party
from unfold.admin import ModelAdmin


@admin.register(ContactUsMessage)
class ContactUsMessageAdmin(ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "message", "status", "date_submitted")
    list_filter = ("status", "date_submitted")
    list_editable = ("status",)
    search_fields = ("first_name", "last_name", "email")
    readonly_fields = ("first_name", "last_name", "email", "message", "date_submitted")

    def has_add_permission(self, request):
        return False


@admin.register(VolunteerSector)
class VolunteerSectorAdmin(ModelAdmin):
    list_display = ("id",)


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "status")
    list_filter = ("status", "date_submitted")
    list_editable = ("status",)
    search_fields = ("first_name", "last_name", "email")

    def has_add_permission(self, request):
        return False
