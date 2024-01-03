from django.urls import path

from FirstApp.views import index

urlpatterns = [
    path('', index),
]
