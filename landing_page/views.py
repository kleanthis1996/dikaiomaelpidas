from django.shortcuts import render


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
    context = {}
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

def team(request, lang="en"):
    """
    This view is used to render the support page
    :param lang:
    :param request:
    :return:
    """
    template = "landing_page/team.html"
    context = {}
    return render(request, template, context)
