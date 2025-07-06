from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    
    return render(request, 'booking/index.html')

def about(request):
    return render(request, 'booking/about.html')

def contact(request):
    return render(request, 'booking/contact.html')


def room(request):
    return render(request, 'booking/room.html')


def single_room(request):
    return render(request, 'booking/single_room.html')


def blog(request):
    
    return render(request, 'booking/blog.html')


def single_blog(request):
    return render(request, 'booking/single_blog.html')
