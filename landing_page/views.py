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
