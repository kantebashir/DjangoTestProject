#from django
from django.contrib import admin
from django.urls import path, include

#for the programmer
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('articles', include('articles.urls')),
    path('about', views.about, name='about'),
    
]
    