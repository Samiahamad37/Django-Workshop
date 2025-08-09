from django.shortcuts import render
from .models import Post


def post_list(request):
    return render(request, 'Workshop/post_list.html',{})