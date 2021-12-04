from django.contrib import admin
from home.models import Setting, ContactFormMessage

class ContractFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message', 'note', 'status']
    list_filter = ['status']
    search_fields = ['name', 'email', 'subject', 'message', 'note']

admin.site.register(ContactFormMessage, ContractFormMessageAdmin)
admin.site.register(Setting)