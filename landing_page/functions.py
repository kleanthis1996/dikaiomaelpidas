from news_and_events.models import PostCategory, Post, PostVariation
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
            "job_role_code": member.job_role.code,
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
            post_content = post_variation.content
            if post_variation:
                response.append({
                    "id": post.id,
                    "title": post.title,
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