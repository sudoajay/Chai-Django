from django.db import models

class Profile(models.Model):
    # Basic fields
    user_name = models.CharField(max_length=100, unique=True)  # Unique username field
    email = models.EmailField()  # Email field with validation
    birth_date = models.DateField()  # Date field for storing dates

    # Optional fields
    bio = models.TextField(blank=True)  # Text field for biography, can be empty

    # File field
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Image upload

    # File field
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)  # General file upload

    def __str__(self):
        return self.user_name

class Product(models.Model):
    # Basic fields
    name = models.CharField(max_length=200)  # Product name
    description = models.TextField()  # Detailed description
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with decimal precision

    # Optional fields
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)  # Product image upload
    stock = models.PositiveIntegerField(default=0)  # Positive integer field for stock quantity

    def __str__(self):
        return self.name

class Document(models.Model):
    # Basic fields
    title = models.CharField(max_length=255)  # Document title
    upload_date = models.DateTimeField(auto_now_add=True)  # Timestamp of when the document was uploaded

    # File field
    file = models.FileField(upload_to='documents/')  # Document file upload

    def __str__(self):
        return self.title

class Event(models.Model):
    # Basic fields
    event_name = models.CharField(max_length=200)  # Name of the event
    event_date = models.DateTimeField()  # Date and time of the event

    # Optional fields
    location = models.CharField(max_length=255, blank=True)  # Event location
    description = models.TextField(blank=True)  # Event description

    def __str__(self):
        return self.event_name
