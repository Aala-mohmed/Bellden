from django.shortcuts import render

# Create your views here.
def specials(request):
    return render(request,'specials/specials.html',{})