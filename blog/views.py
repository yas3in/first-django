from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_blog(request):
    text = """
    Hello! this is for blog in first django web. thank you.
    """
    return HttpResponse(text)


def list_number(request, number):
    #The number argument is the same variable that we took(use) in path
    text = f"""
    this is list {number}
    """
    return HttpResponse(text)


def blog_pages(request):
    return HttpResponse("Blog pages: ")

#sum numbers in url
def sum_number(request, number):
    numbers = str(number.replace("-", " "))
    numbers = numbers.split(" ")
    numbers = (int(number) for number in numbers)
    new_list = []
    for number in numbers:
        new_list.append(number)
    sum = new_list[0] + new_list[1]
    return HttpResponse(f" sum : {sum}")
    