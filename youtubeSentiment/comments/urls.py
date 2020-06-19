from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from comments.views import processUrl

urlpatterns = [
    url(r'^processurl', processUrl, name='processUrl')
]
