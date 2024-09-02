from django.shortcuts import render
from django.http import HttpResponse


def products(requests):
    return HttpResponse("Products: ")
