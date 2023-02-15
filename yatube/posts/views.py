from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    title = 'Последние обновления на сайте'
    text = 'Последние обновления'
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    title = f"Здесь будет информация о группах проекта Yatube {slug}."
    text = f"Здесь будет информация {slug}."
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': title,
        'text': text,
        'group': group,
        'posts': posts,
    }

    return render(request, 'posts/group_list.html', context)