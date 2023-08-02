from django.contrib import admin
from userdashboard.models import customerprofile, service_Detail

# CHANGING ADMIN TITLES
admin.site.site_title = 'UTAWALA SGMS'
admin.site.site_header = 'UTAWALA SGMS'
admin.site.index_title = 'USGMS ADMIN'

# CHANGING TABLE LAYOUT
class service_DetailAdmin(admin.ModelAdmin):
    list_display = ('servicename', 'servicedescription', 'cost', 'creationdate')

# Register your models here.
admin.site.register(customerprofile)
admin.site.register(service_Detail, service_DetailAdmin)
