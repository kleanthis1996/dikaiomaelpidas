# django
from django.contrib import admin
# local
from client_messages.models import ContactUsMessage, VolunteerApplication, VolunteerSector
from translations.functions import get_english_text
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
    list_display = ("id", "get_name", "get_volunteer_applications")

    def get_name(self, obj):
        return get_english_text(obj.name)

    get_name.short_description = "Name"

    def get_volunteer_applications(self, obj):
        return VolunteerApplication.objects.filter(volunteer_sector=obj)

    get_volunteer_applications.short_description = "Volunteer Applications"


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "status")
    list_filter = ("status", "date_submitted")
    list_editable = ("status",)
    search_fields = ("first_name", "last_name", "email")
    readonly_fields = (
        "first_name", "last_name", "email", "date_of_birth", "home_address", "phone_number", "volunteer_sectors",
        "experience_description", "consent_given")

    def has_add_permission(self, request):
        return False
