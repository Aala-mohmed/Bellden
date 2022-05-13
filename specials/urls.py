from django.urls import path
from . import views


urlpatterns = [
    path('', views.specials, name='specials'),
]
