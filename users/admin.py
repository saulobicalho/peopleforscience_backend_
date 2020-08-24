from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Profile


# Unregister the provided model admin
admin.site.unregister(User)

# Register out own model admin, based on the default UserAdmin
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
        'last_login',
        'username',
        'first_name', 'last_name', 'email',
        'is_superuser',
    ]



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = [
        'user',
        'image'
    ]
