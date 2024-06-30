from django.shortcuts import render


# Create your views here

def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def books(request):
    return render(request, 'books.html')



def author(request):
    return render(request, 'author.html')
