from django.shortcuts import render

# Create your views here.
def harrypotter(request):
    return render(request,'harrypotter.html')