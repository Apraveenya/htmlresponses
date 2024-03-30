from django.urls import path
from motivational.views import *
appname='motivational'
urlpatterns = [
    path('youcan/',youcan,name='youcan'),
]