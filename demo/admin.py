from django.contrib import admin
from demo.models import *

admin.site.register(Report, admin.ModelAdmin)
admin.site.register(Content, admin.ModelAdmin)
