from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from livegraph.models import SiteAvailability


class SiteAvailabilityView(View):
    """
    This is the homepage view.
    """

    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class SiteAvailabilityAjaxView(View):
    """
    This is for ajax request.
    The most recent 20 records is being fetched and again reversed to maintain the order of occurrence.
    A json response is sent back containing list of records.
    """

    def get(self, request):
        site_data = SiteAvailability.objects.values(
            "is_uptime", "status", "created_at"
        ).order_by("-created_at")[:20]
        availability = list(site_data)
        availability.reverse()
        return JsonResponse(availability, safe=False)
