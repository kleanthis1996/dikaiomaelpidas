# django
from django.contrib import admin
from django.utils.safestring import mark_safe
# local
from programs.models import Program
from translations.functions import get_english_text
# third party
from unfold.admin import ModelAdmin


@admin.register(Program)
class EducationProgram(ModelAdmin):
    list_display = ("id", "get_name", "get_description", "get_image")

    def get_name(self, obj):
        return get_english_text(obj.name)

    get_name.short_description = "Name"

    def get_description(self, obj):
        return get_english_text(obj.description)

    get_description.short_description = "Description"

    def get_image(self, obj):
        return mark_safe(f'<img src="/mediafiles/{obj.image}" width="50" height="30" />')

    get_image.short_description = "Image"
