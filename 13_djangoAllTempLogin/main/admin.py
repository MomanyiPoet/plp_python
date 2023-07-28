from django.contrib import admin
from main.models import aboutDetail, contactDetail

# CHANGING ADMIN TITLES
admin.site.site_title = 'UTAWALA SGMS'
admin.site.site_header = 'UTAWALA SERVICE GARAGE MANAGEMENT SYSTEM'
admin.site.index_title = 'USGMS ADMIN'

# CHANGING TABLE LAYOUT
class aboutDetailAdmin(admin.ModelAdmin):
    list_display = ('pageName', 'pageDescription')

class contactDetailAdmin(admin.ModelAdmin):
    list_display = ('pagename', 'email', 'mobile', 'address', 'timing')

# Register your models here.
admin.site.register(aboutDetail, aboutDetailAdmin)
admin.site.register(contactDetail, contactDetailAdmin)
