from django.shortcuts import render, redirect

def testhome(request):
    context = {}
    template = "navbar.html"
    return render(request, template, context)

