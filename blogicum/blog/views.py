from django.http import Http404
from django.shortcuts import render

from blog.sources import posts
from common.utils import get_post_by_id, IdNotFoundError


def index(request):
    template = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    try:
        context = {'post': get_post_by_id(posts, id)}
    except IdNotFoundError:
        raise Http404(f'There is no post with id: {id}')
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
