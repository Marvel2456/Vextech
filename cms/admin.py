from django.contrib import admin
from .models import Project, Service, Visit, ContactMessage, NewsletterSubscription, CustomUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

# Register your models here.
User = get_user_model()

# admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm

    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'name')
    ordering = ('email',)
    filter_horizontal = ()
    fieldsets = (
        (None, {'fields': ('email', 'name', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass



@admin.register(Project)
class ProjectAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title',)
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Visit)
class VisitAdmin(ModelAdmin):
    list_display = ('source', 'visited_at', 'ip_address')
    search_fields = ('source', 'user_agent', 'ip_address')
    list_filter = ('source', 'visited_at')
    ordering = ('-visited_at',)


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(ModelAdmin):
    list_display = ('email', 'is_subscribed', 'subscribed_at')
    search_fields = ('email',)
    list_filter = ('is_subscribed', 'subscribed_at')
    ordering = ('-subscribed_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(ModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('sent_at',)
    ordering = ('-sent_at',)
    
    def email(self, obj):
        return obj.email if obj.email else "No Email"
    
    email.short_description = 'Email Address'