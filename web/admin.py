from django.contrib import admin
from web.models import Contact
# Register your models here.


class PersonaAdmin (admin.ModelAdmin):
    pass


admin.site.register(Contact,PersonaAdmin)
