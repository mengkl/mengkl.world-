from django.db.models import Q, Count
from django.http import JsonResponse
from django.shortcuts import render

from index.models import Myapp
from passage.models import Passage, Tag


# Create your views here.


def search_index(request):
    tags_with_counts = Tag.objects.annotate(passages_count=Count('passages'))
    myapp = Myapp
    app_name = myapp.objects.all()
    context = {
        "tags_with_counts": tags_with_counts,
        "app_name": app_name,
    }
    return render(request, "search.html", context)


def search_by_keyword(request, keyword):
    passages = Passage.objects.filter(
        Q(title__icontains=keyword) |  # 匹配标题（部分匹配，不区分大小写）下同
        Q(tags__name__icontains=keyword) |  # 匹配标签名
        Q(abstract__icontains=keyword) |  # 匹配摘要
        Q(body__icontains=keyword)  # 匹配正文
    ).distinct()  # 使用 distinct() 去除重复结果
    data = []
    for passage in passages:
        data.append({
            'status': 'success',
            'title': passage.title,
            'pid': passage.pid,
        })
    return JsonResponse(data, safe=False)


def search_by_tag_name(request, tag_name):
    passages = Passage.objects.filter(tags__name=tag_name)
    data = []
    for passage in passages:
        data.append({
            'status': 'success',
            'title': passage.title,
            'pid': passage.pid,
        })
    return JsonResponse(data, safe=False)


def search_from_passage(request, tag_name):
    tags_with_counts = Tag.objects.annotate(passages_count=Count('passages'))
    passages = Passage.objects.filter(tags__name=tag_name)
    app_name = Myapp.objects.all()
    data = []
    for passage in passages:
        data.append({'pid': passage.pid, 'title': passage.title})
    context = {
        "tags_with_counts": tags_with_counts,
        "app_name": app_name,
        "tag_name_from_passage": tag_name,
        "data": data,
    }
    return render(request, "search.html", context)
