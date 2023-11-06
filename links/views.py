from django.shortcuts import render

from index.models import Myapps
from .models import Friend


# Create your views here.


def links(request):
    links_data = Friend.objects.all()
    app_name = Myapps.objects.all()
    context = {
        "links_data": links_data,
        "app_name": app_name,
    }

    return render(request, "links.html", context)
