from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def aboutus(request):
    return render(request, 'aboutus.html')


def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')
