from django.shortcuts import render

# Create your views here.
def listchefs(request):
    return render(request,'chefs/chefs.html',{})