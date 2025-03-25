# django
from django.contrib import admin
from django.utils.safestring import mark_safe
# local
from team_members.models import JobRole, Member, MemberCategory
from translations.functions import get_english_text
# third party
from unfold.admin import ModelAdmin


@admin.register(JobRole)
class JobRoleAdmin(ModelAdmin):
    list_display = ("id", "get_name", "get_number_of_people")

    def get_number_of_people(self, obj):
        return Member.objects.filter(job_role=obj).count()
    get_number_of_people.short_description = "Number of people"

    def get_name(self, obj):
        return get_english_text(obj.name)
    get_name.short_description = "Name"

@admin.register(MemberCategory)
class MemberCategoryAdmin(ModelAdmin):
    list_display = ("id", "get_name", "get_number_of_people")

    def get_number_of_people(self, obj):
        return Member.objects.filter(category=obj).count()
    get_number_of_people.short_description = "Number of people"

    def get_name(self, obj):
        return get_english_text(obj.name)
    get_name.short_description = "Name"

@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = ("id", "full_name", "job_role", "status", "get_profile_image")
    list_filter = ("job_role", "status")
    search_fields = ("full_name",)

    def get_profile_image(self, obj):
        return mark_safe(f'<img src="/mediafiles/{obj.profile_image}" width="50" height="30" />')

    get_profile_image.short_description = 'Profile image'
