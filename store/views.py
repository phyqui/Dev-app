from django.shortcuts import render, redirect

from django.http import HttpResponse


# Home
def home(request):
    return render(request, "Store/index.html")
