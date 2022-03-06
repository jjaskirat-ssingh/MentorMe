from django.contrib import admin
from .models import Mentor

class MentorAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'department', 'interests')
  list_display_links = ('id', 'name')
  search_fields = ('id', 'name', 'department', 'interests', 'email')
  list_per_page = 25

admin.site.register(Mentor, MentorAdmin)
