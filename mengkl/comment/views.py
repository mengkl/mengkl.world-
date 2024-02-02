import json

from django.http import JsonResponse

from comment.models import Comment
from passage.models import Passage


# Create your views here.
def comment_add(request, pid):
    if request.method == "POST":
        # 获取文章
        passage = Passage.objects.get(pid=pid)
        # 获取评论数据

        post_body = json.loads(request.body)
        comment = post_body.get('comment')
        commentator = post_body.get('commentator')
        commentator_website = post_body.get('commentator_website')

        # 创建并保存评论
        new_comment = Comments.objects.create(
            passage=passage,
            commentator=commentator,
            comment=comment,
            commentator_website=commentator_website,
        )

        data = {
            "status": "success",
            'id': new_comment.id,
            'comment': new_comment.comment,
            'commentator': new_comment.commentator,
            'commentator_website':commentator_website,
            'created_time': new_comment.created_time.strftime('%Y年%m月%d日 %H:%M'),
        }
        return JsonResponse(data)
