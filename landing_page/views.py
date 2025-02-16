from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from landing_page.functions import get_team_members_data, get_posts_data, get_single_post_data


def index(request, lang="en"):
    """
    This view is used to render the index.html
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/index.html"
    context = {}
    return render(request, template, context)


def about(request, lang="en"):
    """
    This view is used to render the about page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/about.html"
    context = {}
    return render(request, template, context)


def services(request, lang="en"):
    """
    This view is used to render the services page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/services.html"
    context = {}
    return render(request, template, context)


def posts_list(request, lang="en", page=1):
    """
    This view is used to render the events page
    :param page:
    :param lang:
    :param request:
    :return:
    """
    # Get full URL from request, to determine content logic
    full_url = request.get_full_path()
    if "events" in full_url:
        template = "landing_page/events.html"
        posts_category = "events_category"
    elif "news" in full_url:
        template = "landing_page/news.html"
        posts_category = "news_category"
    else:
        # In case of wrong url usage, send user to homepage
        return redirect(reverse("landing_page:index"))

    # Get all posts data
    posts_data = get_posts_data(lang, posts_category)
    # Paginate based on requested page
    posts_paginator = Paginator(posts_data, 12)
    posts_current_page = posts_paginator.get_page(page)
    context = {"posts_data": posts_current_page}
    return render(request, template, context)

def posts_detail(request, lang="en", post_id=None):
    """
    View used to handle single post view
    :param request:
    :param lang:
    :param post_id:
    :return:
    """
    # Get full URL from request, to determine content logic
    full_url = request.get_full_path()
    if "event" in full_url:
        # Redirect to homepage if post detail is accessed without id
        if not post_id:
            return redirect(reverse("landing_page:events"))
    elif "news" in full_url:
        # Redirect to homepage if post detail is accessed without id
        if not post_id:
            return redirect(reverse("landing_page:news"))
    else:
        return redirect(reverse("landing_page:index"))
    post_data = get_single_post_data(lang, post_id)



def contact(request, lang="en"):
    """
    This view is used to render the contact page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/contact.html"
    context = {}
    return render(request, template, context)


def support(request, lang="en"):
    """
    This view is used to render the support page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/support.html"
    context = {}
    return render(request, template, context)

def team(request, lang="en"):
    """
    This view is used to render the support page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/team.html"
    team_members_data = get_team_members_data()
    context = {"team_members_data": team_members_data}
    return render(request, template, context)
