# path name to the �index� function in �views.py�
#from django.urls import path
#from . import views
from django.conf.urls import url
from .views import home, success

urlpatterns = [
#    path('', views.index, name='index'),
     url('success/', success),
     url('^$', home)
]