from django.contrib import admin

from .models import *


class TalonsAdmin(admin.ModelAdmin):
    list_display = ('Id_of_doctor', 'DataTime', 'Id_of_patient', 'Title', 'Price')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('pk','First_name', 'Last_name', 'Surname', 'Login', 'Title')


admin.site.register(Users, UsersAdmin)
admin.site.register(Analysis)
admin.site.register(Items)
admin.site.register(Talons, TalonsAdmin)