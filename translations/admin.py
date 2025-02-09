from django.contrib import admin
from translations.models import Translation, Language, Slug


class TranslationInline(admin.StackedInline):
    model = Translation
    extra = 0

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ("code", "name")


@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ("language", "text")
    list_filter = ("language",)
    search_fields = ("text",)


@admin.register(Slug)
class SlugAdmin(admin.ModelAdmin):
    list_display = ("code", "description",)
    search_fields = ("code", "description")
    inlines = [TranslationInline]
