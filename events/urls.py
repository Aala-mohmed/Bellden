from django.urls import path
from . import views


urlpatterns = [
    path('', views.viewevents, name='events'),
]
