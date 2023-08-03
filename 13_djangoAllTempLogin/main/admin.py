from django.contrib import admin
from main.models import aboutDetail, contactDetail, contactUs

# CHANGING TABLE LAYOUT
class aboutDetailAdmin(admin.ModelAdmin):
    list_display = ('pageName', 'pageDescription')

class contactDetailAdmin(admin.ModelAdmin):
    list_display = ('pagename', 'email', 'mobile', 'address', 'timing')

class contactUsAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'mobile', 'message')

# Register your models here.
admin.site.register(aboutDetail, aboutDetailAdmin)
admin.site.register(contactDetail, contactDetailAdmin)
admin.site.register(contactUs, contactUsAdmin)
