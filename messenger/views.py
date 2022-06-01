from django.shortcuts import render

def home(request):
    return render(request,"homepage.html")

def status(request):
    return render(request,"statuspage.html")   


def calls(request):
    return render(request,"callpages.html")     
