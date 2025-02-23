# django
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
# local
from landing_page.functions import get_team_members_data, get_posts_data, get_single_post_data, \
    get_available_programs_data
from translations.decorators import get_translations_information
from webtools.decorators import get_contact_information


@get_contact_information
@get_translations_information
def index(request, lang="en"):
    """
    This view is used to render the index.html
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/index.html"
    available_programs = get_available_programs_data()
    context = {"contact_information": request.contact_information,
               "available_programs": available_programs}
    return render(request, template, context)


@get_contact_information
@get_translations_information
def about(request, lang="en"):
    """
    This view is used to render the about page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/about.html"
    context = {"contact_information": request.contact_information}
    return render(request, template, context)


@get_contact_information
@get_translations_information
def services(request, lang="en"):
    """
    This view is used to render the services page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/services.html"
    available_programs = get_available_programs_data()
    context = {"contact_information": request.contact_information,
               "available_programs": available_programs}
    return render(request, template, context)


@get_contact_information
@get_translations_information
def posts_list(request, lang="en", page=1):
    """
    This view is used to render the events page
    :param page:
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/posts_list.html"
    # Get full URL from request, to determine content logic
    full_url = request.get_full_path()
    if "events" in full_url:
        posts_category = "events_category"
    elif "news" in full_url:
        posts_category = "news_category"
    else:
        # In case of wrong url usage, send user to homepage
        return redirect(reverse("landing_page:index", kwargs={"lang": lang}))

    # Get all posts data
    posts_data = get_posts_data(lang, posts_category)
    # Paginate based on requested page
    posts_paginator = Paginator(posts_data, 3)
    posts_current_page = posts_paginator.get_page(page)
    context = {"contact_information": request.contact_information,
               "posts_data": posts_current_page}
    return render(request, template, context)


@get_contact_information
@get_translations_information
def posts_detail(request, lang="en", post_id=None):
    """
    View used to handle single post view
    :param request:
    :param lang:
    :param post_id:
    :return:
    """
    template = "landing_page/post_detail.html"
    # Get full URL from request, to determine content logic
    full_url = request.get_full_path()
    if "event" in full_url:
        # Redirect to homepage if post detail is accessed without id
        if not post_id:
            return redirect(reverse("landing_page:events", kwargs={"lang": lang, "page": 1}))
        posts_category = "events_category"
    elif "new" in full_url:
        # Redirect to homepage if post detail is accessed without id
        if not post_id:
            return redirect(reverse("landing_page:news", kwargs={"lang": lang, "page": 1}))
        posts_category = "news_category"
    else:
        return redirect(reverse("landing_page:index", kwargs={"lang": lang}))
    post_data = get_single_post_data(lang, post_id)
    # If no post data found redirect to the correct post page
    if not post_data:
        if "event" in full_url:
            return redirect(reverse("landing_page:events", kwargs={"lang": lang, "page": 1}))
        elif "new" in full_url:
            return redirect(reverse("landing_page:news", kwargs={"lang": lang, "page": 1}))

    # Get more articles data
    posts_data = get_posts_data(lang, posts_category)
    # Paginate based on requested page
    posts_paginator = Paginator(posts_data, 12)
    extra_posts = posts_paginator.get_page(1)
    context = {"contact_information": request.contact_information,
               "post_data": post_data,
               "extra_posts": extra_posts}
    return render(request, template, context)


@get_contact_information
@get_translations_information
def contact(request, lang="en"):
    """
    This view is used to render the contact page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/contact.html"
    context = {"contact_information": request.contact_information}
    return render(request, template, context)


@get_contact_information
@get_translations_information
def support(request, lang="en"):
    """
    This view is used to render the support page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/support.html"
    context = {"contact_information": request.contact_information}
    return render(request, template, context)


@get_contact_information
@get_translations_information
def team(request, lang="en"):
    """
    This view is used to render the support page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/team.html"
    team_members_data = get_team_members_data()
    context = {"contact_information": request.contact_information,
               "team_members_data": team_members_data}
    return render(request, template, context)
