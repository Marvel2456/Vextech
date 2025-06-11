from django.shortcuts import render

# Create your views here.


def IndexView(request):
    return render(request, 'pages/index.html')

def AboutView(request):
    return render(request, 'pages/about.html')

def ContactView(request):
    return render(request, 'pages/contact.html')

def ServicesView(request):
    return render(request, 'pages/services.html')

def ProjectsView(request):
    return render(request, 'pages/projects.html')