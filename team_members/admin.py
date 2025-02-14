# django
from django.contrib import admin
from django.utils.safestring import mark_safe

# local
from team_members.models import JobRole, Member
# third party
from unfold.admin import ModelAdmin, StackedInline

class TeamMemberAdminInline(StackedInline):
    model = Member
    extra = 1

@admin.register(JobRole)
class JobRoleAdmin(ModelAdmin):
    list_display = ("code", "name", "get_number_of_people")
    search_fields = ("code", )

    inlines = [TeamMemberAdminInline]

    def get_number_of_people(self, obj):
        number_of_people = Member.objects.filter(job_role=obj).count()
        return number_of_people
    get_number_of_people.short_description = "Number of people"



@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = ("full_name", "job_role", "status","get_profile_image" )
    list_filter = ("job_role", "status")
    search_fields = ("full_name",)

    def get_profile_image(self, obj):
            return mark_safe(f'<img src="/mediafiles/{obj.profile_image}" width="50" height="30" />')
    get_profile_image.short_description = 'Profile image'
