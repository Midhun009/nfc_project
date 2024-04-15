from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'checkedin', 'age', 'phone', 'email','sex' )  

admin.site.register(Profile, ProfileAdmin)

