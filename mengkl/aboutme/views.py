import markdown
from django.shortcuts import render

from index.models import Myapp
from .models import AboutMe

extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.abbr',
              'markdown.extensions.attr_list', 'markdown.extensions.def_list', 'markdown.extensions.fenced_code',
              'markdown.extensions.footnotes', 'markdown.extensions.md_in_html', 'markdown.extensions.tables',
              'markdown.extensions.admonition', 'markdown.extensions.legacy_attrs', 'markdown.extensions.legacy_em',
              'markdown.extensions.meta', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists',
              'markdown.extensions.smarty', 'markdown.extensions.toc', 'markdown.extensions.wikilinks',
              'markdown_del_ins', ]


# Create your views here.

def about_me(request):
    a = AboutMe.objects.all()
    app_name = Myapp.objects.all()

    for raw_body in a:
        raw_body.body_after_changed = markdown.markdown(raw_body.body, extensions=extensions)
        raw_body.save()

    elements = AboutMe.objects.all()

    context = {
        "elements": elements,
        "app_name": app_name,
    }
    return render(request, "aboutme.html", context)
