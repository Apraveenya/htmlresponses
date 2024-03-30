from django.urls import path
from fictional.views import *
appname='fictional'
urlpatterns = [
    path('harrypotter/',harrypotter,name='harrypotter'),
]