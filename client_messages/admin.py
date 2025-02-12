from django.contrib import admin

from client_messages.models import ContactUsMessage

from unfold.admin import ModelAdmin


@admin.register(ContactUsMessage)
class ContactUsMessageAdmin(ModelAdmin):
    list_display = ("first_name", "last_name", "email", "message", "status", "date_submitted")
    list_filter = ("status", "date_submitted")
    list_editable = ("status",)
    search_fields = ("first_name", "last_name", "email")
