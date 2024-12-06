from django.contrib import admin
from .models import Profile, Product, Document, Event

class ProfileAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('user_name', 'email', 'birth_date', 'profile_picture', 'resume')
    
    # Fields to add search functionality
    search_fields = ('user_name', 'email')
    
    # Optional: Filter by fields in the list view
    list_filter = ('birth_date',)

    # Optional: Add pagination
    list_per_page = 20  # Number of items per page

class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'price', 'stock', 'image')
    
    # Fields to add search functionality
    search_fields = ('name', 'description')
    
    # Optional: Filter by fields in the list view
    list_filter = ('price', 'stock')

    # Optional: Add pagination
    list_per_page = 20  # Number of items per page

class DocumentAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'upload_date', 'file')
    
    # Fields to add search functionality
    search_fields = ('title',)
    
    # Optional: Add pagination
    list_per_page = 20  # Number of items per page

class EventAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('event_name', 'event_date', 'location', 'description')
    
    # Fields to add search functionality
    search_fields = ('event_name', 'location')
    
    # Optional: Filter by fields in the list view
    list_filter = ('event_date',)

    # Optional: Add pagination
    list_per_page = 20  # Number of items per page

# Register models with their corresponding admin classes
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Event, EventAdmin)
