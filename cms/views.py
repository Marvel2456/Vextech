from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import ContactMessage, NewsletterSubscription, Visit, Service, Project

from django.template.response import TemplateResponse


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
            # Print form errors to console for debugging
            print("Form errors:", form.errors)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'cms/register.html', {'form': form})
def loginView(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)  # Use renamed function
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
    
    return render(request, 'cms/login.html')


@login_required(login_url='login')
def logoutView(request):
    if request.method == 'POST':
        auth_logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')
    
    return TemplateResponse(request, 'cms/logout.html', {})



@login_required(login_url='login')
def dashboard(request):
    context = {
        "first_name": request.user.name.split()[0]
    }
    return render(request, 'cms/dashboard.html', context)


def viewContact(request):
    contacts = ContactMessage.objects.all()
    return render(request, 'cms/contacts.html', {'contacts': contacts})


def NewsletterView(request):
    subscriptions = NewsletterSubscription.objects.all()
    return render(request, 'cms/newsletter.html', {'subscriptions': subscriptions})


def viewVisits(request):
    visits = Visit.objects.all()
    return render(request, 'cms/visits.html', {'visits': visits})


def viewServices(request):
    services = Service.objects.all()
    return render(request, 'cms/services.html', {'services': services})


def loadProjectModal(request):
    return render(request, 'modals/create_project.html')

def createProject(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        project_type = request.POST.get('project_type')
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        link = request.POST.get('link')
        is_featured = request.POST.get('is_featured') == 'on'
        
        project = Project(
            name=name,
            project_type=project_type,
            title=title,
            description=description,
            image=image,
            link=link,
            is_featured=is_featured
        )
        project.save()

        messages.success(request, 'Project created successfully!')
        return HttpResponse('<div id="modal" class="hidden"></div><script>location.reload()</script>')

    # For GET (to render modal form)
    return render(request, 'modal/create_project.html')


def loadEditProjectModal(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'modals/edit_project.html', {'project': project})

def editProject(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.name = request.POST.get('name')
        project.project_type = request.POST.get('project_type')
        project.title = request.POST.get('title')
        project.description = request.POST.get('description')
        project.link = request.POST.get('link')
        if request.FILES.get('image'):
            project.image = request.FILES['image']
        project.save()
        # Optionally, you can return a snippet to close the modal or refresh the project list
        # return render(request, 'partials/success_message.html', {'message': 'Project updated!'})

        messages.success(request, 'Project updated successfully!')
        return HttpResponse('<div id="modal" class="hidden"></div><script>location.reload()</script>')
    
def loadDeleteProjectModal(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'modals/delete_project.html', {'project': project})

def deleteProject(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        # Optionally, return a snippet to close the modal or refresh the project list
        # return render(request, 'partials/success_message.html', {'message': 'Project deleted!'})
        messages.success(request, 'Project deleted successfully!')
        return HttpResponse('<div id="modal" class="hidden"></div><script>location.reload()</script>')
    # return render(request, 'modals/delete_project.html', {'project': project})
    
# def createProject(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         project_type = request.POST.get('project_type')
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         image = request.FILES.get('image')
#         link = request.POST.get('link')
#         is_featured = request.POST.get('is_featured') == 'on'
        
#         project = Project(
#             name=name,
#             project_type=project_type,
#             title=title,
#             description=description,
#             image=image,
#             link=link,
#             is_featured=is_featured
#         )
#         project.save()

        
#         messages.success(request, 'Project created successfully!')
        
#         return HttpResponse(render(request, 'modals/create_project.html', {'project': project}))


def viewProjects(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
        'first_name': request.user.name.split()[0]
    }
    return render(request, 'cms/projects.html', context)

# def viewProject(request, slug):
#     try:
#         project = Project.objects.get(slug=slug)
#     except Project.DoesNotExist:
#         messages.error(request, 'Project not found.')
#         return redirect('view_projects')
    
#     return render(request, 'cms/project_detail.html', {'project': project})
