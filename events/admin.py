from django.contrib import admin
from .models import event


# Register your models here.
class eventAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class meta:
        model = event


admin.site.register(event)
