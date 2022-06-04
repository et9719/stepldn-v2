''' Imports '''
from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    ''' Define what admin should see in contact part of admin page '''
    list_display = (
        'subject',
        'email',
    )


admin.site.register(Contact, ContactAdmin)
