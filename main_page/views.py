from django.shortcuts import render_to_response
from main_page.models import Post, Comment


def blog(request):
    return render_to_response('blog.html', {'posts': Post.objects.all()}, {'comments': Comment.objects.all()})
