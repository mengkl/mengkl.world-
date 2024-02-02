import markdown
from django.shortcuts import render

from comment.models import Comment
from index.models import Myapp
from passage.models import Passage, Tag


# Create your views here.

def passage_show(request, pid):
    passage = Passage.objects.get(pid=pid)
    comment = Comment.objects.filter(passage__pid=pid)
    tag = Tag.objects.all()
    app_name = Myapp.objects.all()
    passage.body = markdown.markdown(passage.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.abbr',
        'markdown.extensions.attr_list',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.footnotes',
        'markdown.extensions.md_in_html',
        'markdown.extensions.tables',
        'markdown.extensions.admonition',
        'markdown.extensions.legacy_attrs',
        'markdown.extensions.legacy_em',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.sane_lists',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        'markdown.extensions.wikilinks',
        'markdown_del_ins',
    ])
    context = {
        "passage": passage,
        "comment": comment,
        "tag": tag,
        'app_name': app_name,
    }
    return render(request, "passage.html", context)


def passage_index(request):
    passages_data = Passage.objects.values('title', 'pid', 'abstract')
    context = {
        "passages_data": passages_data,
    }
    return render(request, "passage_index.html", context)
