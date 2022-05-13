from django.shortcuts import render

# Create your views here.
def topten(request):
    return render(request,'topten/topten.html',{})