from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from users.models   import CustomUser

class CustomUserAdmin(UserAdmin):
    models = CustomUser
    list_display = ["username", "email", "is_staff"]

admin.site.register(CustomUser, CustomUserAdmin)
