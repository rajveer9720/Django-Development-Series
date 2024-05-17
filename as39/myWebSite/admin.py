from django.contrib import admin

# Register your models here.
from .models import Contact
from .models import Student

class StudentAdmin(admin.ModelAdmin):
   list_display = ('stuid', 'stuname','stuemail', 'stupass',)

admin.site.register(Contact)
admin.site.register(Student, StudentAdmin)