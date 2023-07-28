from django.contrib import admin
from main.models import aboutDetail, contactDetail

# CHANGING TABLE LAYOUT
class aboutDetailAdmin(admin.ModelAdmin):
    list_display = ('pageName', 'pageDescription')

class contactDetailAdmin(admin.ModelAdmin):
    list_display = ('pagename', 'email', 'mobile', 'address', 'timing')

# Register your models here.
admin.site.register(aboutDetail, aboutDetailAdmin)
admin.site.register(contactDetail, contactDetailAdmin)
