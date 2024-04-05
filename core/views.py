from django.shortcuts import render

# Create your views here.
def viewhome(request):
    return render(request, 'home.html')
