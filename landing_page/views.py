from django.shortcuts import render

from landing_page.functions import get_team_members_data, get_posts_data


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


def events(request, lang="en"):
    """
    This view is used to render the events page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/events.html"
    events_data = get_posts_data(lang, "events_category")
    context = {"events_data": events_data}
    return render(request, template, context)


def news(request, lang="en"):
    """
    This view is used to render the news page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/news.html"
    context = {}
    return render(request, template, context)


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


def meet_the_team(request, lang="en"):
    """
    This view is used to render the meet_the_team page
    :param request:
    :param lang:
    :return:
    """
    template = "landing_page/meet_the_team.html"
    team_members_data = get_team_members_data()
    context = {"team_members_data": team_members_data}
    return render(request, template, context)
