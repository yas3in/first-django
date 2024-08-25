from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_blog(request):
    text = """
    Hello! this is for blog in first django web. thank you.
    """
    return HttpResponse(text)


def blog_pages(request):
    return HttpResponse("Blog pages: ")