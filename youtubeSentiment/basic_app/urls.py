from basic_app import views 
from django.urls import path, include
from django.conf.urls import url
app_name='basic_app'
urlpatterns = [
    path('',views.index,name='index'),
    url(r'^register/',views.register,name='register'),
    # url(r'^login/',views.login,name='login'),
]
