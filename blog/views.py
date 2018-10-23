from django.shortcuts import render

posts = [
    {
        'author': 'fjksdaf',
        'title': 'kljfasd',
        'content': 'fsadkfja',
        'date_posted': 'fjkasdhf'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)
