from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    return HttpResponse("Test")

def generate(request):

    request.session['word'] = get_random_string(length=14)
    if request.method == "POST":
        if 'count' not in request.session:
            request.session['count'] = 1
        else:
            request.session['count'] += 1

    return render(request, "random_word/index.html")

def reset(request):
    if request.method == "POST":
        del request.session['count']
    return redirect("/random_word")
