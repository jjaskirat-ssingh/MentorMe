from django.contrib import admin
from .models import Profile

class StudentAdmin(admin.ModelAdmin):
  list_display = ('id', 'user', 'department', 'interests')
  list_display_links = ('id', 'user')
  search_fields = ('id', 'name', 'department', 'interests', 'email')
  list_per_page = 25

admin.site.register(Profile, StudentAdmin)
