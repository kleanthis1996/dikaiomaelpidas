from django.contrib import admin
from translations.models import Translation, Language, Slug


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("code", "name")


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("language", "text")


@admin.register(Slug)
class SlugAdmin(admin.ModelAdmin):
    list_display = ("code", "description", "get_available_translations")

    def get_available_translations(self, obj):
        available_translations = []
        for translation in obj.translations.all():
            available_translations.append(translation.language.code)
        return available_translations
    get_available_translations.short_description = "Available translations"