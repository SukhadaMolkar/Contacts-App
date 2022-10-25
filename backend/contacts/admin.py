from django.contrib import admin
from .models import Contact
# Register your models here.


# @admin_register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display=["id","country_code","first_name","last_name","phone_number"]

admin.site.register(Contact,AdminContact)
