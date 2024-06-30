from django.urls import path
from .views import home, login, register, books, author

urlpatterns = [
    path('', home, name='home.html'),
    path('login/', login, name='login.html'),
    path('register/', register, name='register.html'),
    path('books/', books, name='books.html'),
    path('author/', author, name='author.html'),
]
