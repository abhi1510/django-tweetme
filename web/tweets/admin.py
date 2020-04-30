from django.contrib import admin

from .models import Tweet, Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('tweet', 'sent')

admin.site.register(Tweet)
admin.site.register(Notification, NotificationAdmin)