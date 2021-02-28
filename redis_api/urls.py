from django.urls import path
from .views.api import Communicate

redis_api_url_pattens = [
    path('communicate/server1', Communicate.as_view()),
    path('communicate/server2', Communicate.as_view())
]