from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def blogs(request):
    return render(request, 'blogs.html')
