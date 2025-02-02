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