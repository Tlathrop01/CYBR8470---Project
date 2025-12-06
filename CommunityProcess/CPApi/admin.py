from django.contrib import admin
from .models import Issue, Question, Choice

# Register your models here.

# Adding question to the admin site interface
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    list_display = ["question_text", "owner", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

# Adding choice to the admin site interface
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

admin.site.register(Choice)


class IssueAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('Issue_name', 'description')
    
    # Add search functionality for specific fields
    search_fields = ('Issue_name', 'description')

    # Add filters for the fields in the sidebar
    list_filter = ('Issue_name', 'description')

    # Define which fields can be clicked to view the details page
    list_display_links = ('Issue_name',)

    # Define how fields are displayed when editing an instance
    fields = ('Issue_name', 'description')

# Register the model and admin class
admin.site.register(Issue, IssueAdmin)