from django.shortcuts import render


def index(request):
    return render(request, 'restaurant/index.html', {})

def about(request):
    return render(request, 'restaurant/about.html')