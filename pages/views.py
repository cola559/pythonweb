from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def products(request):
    return render(request, 'pages/products.html')

def contact(request):
    return render(request, 'pages/contact.html')