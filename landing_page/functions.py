# local
from django.urls import reverse_lazy

from news_and_events.models import Post, PostVariation
from programs.models import Program
from team_members.models import Member
from translations.models import Language


def get_team_members_data():
    """
    Function to get team members data from db for meet the team page
    :return:
    """
    team_members_data = Member.objects.select_related("job_role").filter(status=True)
    response = []
    for member in team_members_data:
        response.append({
            "id": member.id,
            "full_name": member.full_name,
            "profile_image_url": member.profile_image.url,
            "description": member.description,
            "job_role_name": member.job_role.name.code,

        })
    return response


def get_posts_data(lang, posts_category):
    """
    Function to get events and news data from db for the events or news page
    :param lang:
    :param posts_category:
    :return:
    """
    response = []
    try:
        # Get language object based on lang
        language = Language.objects.get(code=lang)
        # Get all posts based on category
        posts = Post.objects.filter(category__code=posts_category)
        for post in posts:
            # Get correct variation based on language and if is active
            post_variation = PostVariation.objects.filter(post=post,
                                                          language=language,
                                                          status=True).first()
            # Parse the post detail URL
            post_detail_url = "#"
            if posts_category == "events_category":
                post_detail_url = reverse_lazy("landing_page:event_detail",
                                               kwargs={"lang": lang, "post_id": post.id})
            elif posts_category == "news_category":
                post_detail_url = reverse_lazy("landing_page:new_detail",
                                               kwargs={"lang": lang, "post_id": post.id})
            if post_variation:
                response.append({
                    "id": post.id,
                    "post_detail_url": post_detail_url,
                    "title": post.title.code,
                    "image_url": post.image.url,
                    "published_date": post.published_date,
                })
    except Exception as e:
        print(e)
    return response


def get_single_post_data(lang, post_id):
    """
    Function to get single post data from db for the events or news page
    :param lang:
    :param post_id:
    :return:
    """
    # Get requested post variation
    post_data = PostVariation.objects.filter(post__id=post_id, language__code=lang).first()
    if not post_data:
        return None
    # Prepare result for post detail page
    result = {
        "parent_post_id": post_data.post.id,
        "title": post_data.post.title.code,
        "image_url": post_data.post.image.url,
        "content": post_data.content
    }
    return result


def get_available_programs_data():
    """
    Function to get available programs data from db for programs page
    :return:
    """
    available_programs_data = Program.objects.filter(status=True)
    result = []
    for program in available_programs_data:
        result.append({
            "id": program.id,
            "name": program.name.code,
            "description": program.description,
            "image_url": program.image.url,
        })
    return result