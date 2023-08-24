from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POSTS_COUNT = 5


def index(request):
    template = 'blog/index.html'
    post_list = (
        Post.objects.select_related('category', 'author')
        .prefetch_related('location')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        )[:POSTS_COUNT]
    )
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('category', 'author')
        .prefetch_related('location')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__is_published=True,
        ),
        pk=id,
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug,
    )
    post_list = (
        Post.objects.select_related('category', 'author')
        .prefetch_related('location')
        .filter(
            pub_date__lte=timezone.now(),
            is_published=True,
            category__slug=category_slug,
        )
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
