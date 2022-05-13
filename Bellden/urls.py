"""Bellden URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import imod
from django.contrib import admin
from django.urls import path
from chefs.views import listchefs
from contact.views import contact
from events.views import viewevents
from menu.views import menu
from about.views import about
from gallery.views import gallery
from table.views import table
from specials.views import specials
from topten.views import topten
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chefs/',listchefs ,name="chefs"),
    path('contact/', contact,name="contact"),
    path('events/', viewevents,name="events"),
    path('menu/', menu,name="menu"),
    path('about/', about,name="about"),
    path('gallery/',gallery ,name="gallery"),
    path('table/',table ,name="table"),
    path('specials/',specials ,name="specials"),
    path('topten/',topten ,name="topten"),


]
