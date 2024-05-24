from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def add_user(request):
    return render(request, 'store/create_user.html')