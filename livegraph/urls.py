from django.urls import path

from livegraph.views import SiteAvailabilityAjaxView, SiteAvailabilityView

app_name = "livegraph"

urlpatterns = [
    path("", SiteAvailabilityView.as_view(), name="homepage"),
    path(
        "site-availability-ajax",
        SiteAvailabilityAjaxView.as_view(),
        name="site-availability-ajax",
    ),
]
