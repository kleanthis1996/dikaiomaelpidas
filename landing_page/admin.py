from django.contrib import admin

from landing_page.models import Post, PostCategory, PostVariation

class PostVariationInline(admin.StackedInline):
    model = PostVariation
    extra = 0

@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "internal_name", "get_number_of_posts")

    def get_number_of_posts(self, obj):
        return Post.objects.filter(category=obj).count()
    get_number_of_posts.short_description = "Number of Posts"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "internal_name", "category", "get_status", "published_date")
    inlines = [PostVariationInline]

    def get_status(self, obj):
        is_post_active = PostVariation.objects.filter(status=True)
        if is_post_active:
            return True
        return False
    get_status.short_description = "Status"