from django.shortcuts import render
from cms.models import Project, ContactMessage, NewsletterSubscription
from .forms import ContactMessageForm, NewsletterSubscriptionForm

# Create your views here.


def IndexView(request):
    top_projects = Project.objects.all().order_by('-created_at')
    newsletter_success = False
    contact_success = False
    if request.method == "POST":
        if 'email' in request.POST and 'name' not in request.POST:
            # Newsletter form
            email = request.POST.get('email')
            if email:
                NewsletterSubscription.objects.get_or_create(email=email, is_subscribed=True)
                newsletter_success = True
        elif 'name' in request.POST:
            # Contact form
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            if name and email and subject and message:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                contact_success = True
    context = {
        'top_projects': top_projects,
        'newsletter_success': newsletter_success,
        'contact_success': contact_success,
    }
    return render(request, 'pages/index.html', context)

def AboutView(request):
    return render(request, 'pages/about.html')

def ContactView(request):
    contact_success = False
    if request.method == "POST":
        if 'name' in request.POST:
            # Contact form
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            if name and email and subject and message:
                ContactMessage.objects.create(
                    name=name,
                    email=email,
                    subject=subject,
                    message=message
                )
                contact_success = True
    context = {
        'contact_success': contact_success,
    }
    return render(request, 'pages/contact.html', context)

def ServicesView(request):
    return render(request, 'pages/services.html')

def ProjectsView(request):
    projects = Project.objects.all().order_by('-id')
    context = {
        'projects': projects,
    }
    return render(request, 'pages/projects.html', context)