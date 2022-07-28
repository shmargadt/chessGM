from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, candidate. You're at the chess engine index.")
