from django.contrib import admin

from waitlist.models import WaitList


@admin.register(WaitList)
class WaitListAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'theme')
