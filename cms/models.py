from django.db import models
import uuid
from django.utils.timezone import now
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email




PROJECT_TYPE_CHOICES = [
    ('web', 'Web Development'),
    ('mobile', 'Mobile App Development'),
    ('design', 'Design Services'),
    ('consulting', 'Consulting Services'),
    ('other', 'Other'),
]


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES, default='web')
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.name.lower().replace(' ', '-')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['-created_at']  

class Service(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=200, blank=True, null=True)  # Assuming icon is a string (e.g., font-awesome class name)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Services"
        ordering = ['-created_at']


SOURCE_CHOICES = [
    ('whatsapp', 'WhatsApp'),
    ('instagram', 'Instagram'),
    ('facebook', 'Facebook'),
    ('mobile', 'Mobile'),
    ('tablet', 'Tablet'),
    ('desktop', 'Desktop'),
    ('unknown', 'Unknown'),
]

class Visit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='unknown')
    user_agent = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    visited_at = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.source} - {self.visited_at}"
    


class NewsletterSubscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    is_subscribed = models.BooleanField(default=True, blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Newsletter Subscriptions"
        ordering = ['-subscribed_at']


class ContactMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        verbose_name_plural = "Contact Messages"
        ordering = ['-sent_at']