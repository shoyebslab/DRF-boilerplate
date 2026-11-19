from django.contrib import admin

from .models import UserActivityLog


@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "action", "ip_address", "created_at")
    list_filter = ("action", "created_at")
    search_fields = ("user__email", "user__username", "ip_address", "action")
    readonly_fields = ("id", "user", "action", "ip_address", "user_agent", "created_at", "updated_at")
