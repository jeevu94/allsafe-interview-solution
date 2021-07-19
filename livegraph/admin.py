from django.contrib import admin

from livegraph.models import SiteAvailability


@admin.register(SiteAvailability)
class SiteAvailabilityAdmin(admin.ModelAdmin):
    list_display = ("availability", "status", "created_at")
    list_display_links = ("availability",)
    readonly_fields = ("created_at", "updated_at")
    list_per_page = 20

    def availability(self, obj):
        return "Uptime" if obj.is_uptime else "Downtime"
