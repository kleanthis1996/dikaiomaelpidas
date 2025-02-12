from django.contrib import admin
from translations.models import Translation, Language, Slug

from unfold.admin import ModelAdmin
from unfold.admin import StackedInline

class TranslationInline(StackedInline):
    model = Translation
    extra = 0

@admin.register(Language)
class LanguageAdmin(ModelAdmin):
    list_display = ("code", "name", "status")
    list_filter = ("status",)


@admin.register(Translation)
class TranslationAdmin(ModelAdmin):
    list_display = ("language", "text")
    list_filter = ("language",)
    search_fields = ("text",)


@admin.register(Slug)
class SlugAdmin(ModelAdmin):
    list_display = ("code", "description", "get_available_translation_languages")
    list_filter = ("translation__language",)
    search_fields = ("code", "description")
    inlines = [TranslationInline]

    def get_available_translation_languages(self, obj):
        available_languages = Translation.objects.filter(slug=obj).values_list("language__code", flat=True)
        return list(available_languages)
    get_available_translation_languages.short_description = "Available languages"
