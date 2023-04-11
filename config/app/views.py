from django.shortcuts import render
from django.http import HttpRequest


def index(request: HttpRequest):
    menu_name = request.path
    return render(request, 'app/index.html', {'menu_name': menu_name})
