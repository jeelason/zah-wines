from django.contrib import admin
from wines.models import Wine, Contact  # , Consultan


class ContactAdmin(admin.ModelAdmin):
    pass


# class ConsultantAdmin(admin.ModelAdmin):
#     pass


class WineAdmin(admin.ModelAdmin):
    pass


admin.site.register(Wine, WineAdmin)
admin.site.register(Contact, ContactAdmin)
# admin.site.register(Consultant, ConsultantAdmin)
