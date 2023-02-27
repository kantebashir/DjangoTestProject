#from django
from django.conf.urls import path 

#from programmer
from . import views


urlpatterns = [
    path('', views.article_list, name='article')
]




