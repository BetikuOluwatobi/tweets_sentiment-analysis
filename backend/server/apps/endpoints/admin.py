from django.contrib import admin
from .models import Users_Input
# Register your models here.

@admin.register(Users_Input)
class UsersInputAdmin(admin.ModelAdmin):
  list_display = ['users_input']

