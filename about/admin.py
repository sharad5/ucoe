from django.contrib import admin
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
	list_filter = ['created','modified']
	list_display = ('about','created','modified')

admin.site.register(Department, DepartmentAdmin)
