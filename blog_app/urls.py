from django.urls import path
from .views import get_blog

urlpatterns = [
    path('', get_blog, name='blog'),
]