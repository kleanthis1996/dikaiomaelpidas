from django.shortcuts import render


def index(request):
    """
    This view is used to render the index.html
    :param request:
    :return:
    """
    template = "landing_page/index.html"
    context = {}
    return render(request, template, context)


def about(request):
    """
    This view is used to render the about page
    :param request:
    :return:
    """
    template = "landing_page/about.html"
    context = {}
    return render(request, template, context)


def services(request):
    """
    This view is used to render the services page
    :param request:
    :return:
    """
    template = "landing_page/services.html"
    context = {}
    return render(request, template, context)


def events(request):
    """
    This view is used to render the events page
    :param request:
    :return:
    """
    template = "landing_page/events.html"
    context = {}
    return render(request, template, context)


def news(request):
    """
    This view is used to render the news page
    :param request:
    :return:
    """
    template = "landing_page/news.html"
    context = {}
    return render(request, template, context)


def contact(request):
    """
    This view is used to render the contact page
    :param request:
    :return:
    """
    template = "landing_page/contact.html"
    context = {}
    return render(request, template, context)


def support(request):
    """
    This view is used to render the support page
    :param request:
    :return:
    """
    template = "landing_page/support.html"
    context = {}
    return render(request, template, context)
