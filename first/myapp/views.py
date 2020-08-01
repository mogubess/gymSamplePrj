from django.shortcuts import render


def index(request):
    context = {'name': 'Boku'}
    return render(request, 'myapp/base.html', context=context)
# from django.http import HttpResponse
# import logging

# logging.basicConfig(level=logging.DEBUG)


# def index(request):
# django.core.handlers.wsgi.WSGIRequest
# logging.critical(request.get_host())
# logging.critical(request.get_full_path())
# logging.critical(request.get_full_path_info(force_append_slash=True))
# logging.critical(request.get_raw_uri())
# return HttpResponse("Hello, world")
