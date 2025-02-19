# django
from django.contrib import admin
# local
from .models import Post, PostCategory, PostVariation
from translations.functions import get_english_text
# third party
from unfold.admin import ModelAdmin
from unfold.admin import StackedInline

class PostVariationInline(StackedInline):
    model = PostVariation
    extra = 0
    tab=True


@admin.register(PostCategory)
class PostCategoryAdmin(ModelAdmin):
    list_display = ("id", "get_category_name", "get_number_of_posts")

    def get_number_of_posts(self, obj):
        return Post.objects.filter(category=obj).count()
    get_number_of_posts.short_description = "Number of Posts"

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        return ["code"]

    def get_category_name(self, obj):
        return get_english_text(obj.name)
    get_category_name.short_description = "Name"

@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("id", "get_title", "category", "get_status", "published_date")
    list_filter = ("category",)
    inlines = [PostVariationInline]

    def get_status(self, obj):
        is_post_active = PostVariation.objects.filter(post=obj,status=True)
        if is_post_active:
            return True
        return False
    get_status.short_description = "Status"

    def get_title(self, obj):
        return get_english_text(obj.title)
    get_title.short_description = "Title"