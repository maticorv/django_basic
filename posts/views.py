from datetime import datetime

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def list_posts(request):
    posts = [
        {
            'name': 'My Dog.',
            'user': 'Yésica Cortes',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/id/237/200/200'
        },
        {
            'name': 'Khe.',
            'user': 'Pink Woman',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/id/84/200/200'
        },
        {
            'name': 'Nautural web.',
            'user': 'Pancho Villa',
            'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
            'picture': 'https://picsum.photos/id/784/200/200'
        },
    ]
    content = []
    for post in posts:
        content.append("""
        <p>{name}</p>
        <p>{user}</p>
        <p>{timestamp}</p>
        <figure><img src="{picture}"/></figure>
        """.format(
            name=post.get('name'),
            user=post.get('user'),
            timestamp=post.get('timestamp'),
            picture=post.get('picture'),
            ))
    return HttpResponse('<br>'.join(content))
