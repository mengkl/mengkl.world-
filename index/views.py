import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from comment.models import Comments
from passage.models import Passage
from . import models

extensions = ['markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.abbr',
              'markdown.extensions.attr_list', 'markdown.extensions.def_list', 'markdown.extensions.fenced_code',
              'markdown.extensions.footnotes', 'markdown.extensions.md_in_html', 'markdown.extensions.tables',
              'markdown.extensions.admonition', 'markdown.extensions.legacy_attrs', 'markdown.extensions.legacy_em',
              'markdown.extensions.meta', 'markdown.extensions.nl2br', 'markdown.extensions.sane_lists',
              'markdown.extensions.smarty', 'markdown.extensions.toc', 'markdown.extensions.wikilinks',
              'markdown_del_ins', ]


# Create your views here.

def index_page(request, page_id):
    # 文章分页展示
    page_id = int(page_id)
    passages_query = Passage.objects.order_by('id')  # 获取Passages模型的查询集
    paginator = Paginator(passages_query, 5)  # 实例化一个分页对象, 每页显示5个
    try:
        page_obj = paginator.page(page_id)
    except PageNotAnInteger:
        page_obj = paginator.page(1)  # 如果传入page参数不是整数，默认第一页
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False  # 如果页数小于1不使用分页

    # 文章展示
    raw_abstract = Passage.objects.all()

    # 头部栏
    app_name = models.Myapps.objects.all()

    # 左侧栏数据
    passage_count = str(Passage.objects.all().count()).rjust(9, '0')
    comment_count = str(Comments.objects.all().count()).rjust(9, '0')

    # markdown相关
    for abstract in raw_abstract:
        a = markdown.markdown(abstract.abstract, extensions=extensions)
        abstract.abstract_after_changed = a
        abstract.save()
    passagedata = Passage.objects.all()

    context = {'page_obj': page_obj,
               'is_paginated': is_paginated,
               'app_name': app_name,
               'passages_data': passagedata,
               'passage_count': passage_count,
               'comment_count': comment_count,
               }
    return render(request, "index.html", context)
