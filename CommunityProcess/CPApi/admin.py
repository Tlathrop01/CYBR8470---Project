from django.contrib import admin
from .models import Issue

# Register your models here.


class IssueAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('Issue_name', 'description')
    
    # Add search functionality for specific fields
    search_fields = ('Issue_name', 'description')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('Issue_name', 'description')

    # Define which fields can be clicked to view the details page
    list_display_links = ('Issue_name',)

    # Define how fields are displayed when editing a Dog instance
    fields = ('Issue_name', 'description')

# Register the model and admin class
admin.site.register(Issue, IssueAdmin)