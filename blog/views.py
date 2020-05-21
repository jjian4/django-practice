from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'James',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Aug 27, 2018'
    },
    {
        'author': 'James',
        'title': 'Blog post 2',
        'content': '2nd post content',
        'date_posted': 'Aug 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
