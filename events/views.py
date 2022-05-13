from django.shortcuts import render

# Create your views here.
def viewevents(request):
    return render(request,'events/events.html',{})