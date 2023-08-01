from django.contrib import admin
from userdashboard.models import customerprofile

# CHANGING ADMIN TITLES
admin.site.site_title = 'UTAWALA SGMS'
admin.site.site_header = 'UTAWALA SGMS'
admin.site.index_title = 'USGMS ADMIN'

# Register your models here.
admin.site.register(customerprofile)
