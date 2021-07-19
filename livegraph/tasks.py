import requests

from allsafe.celery import app
from livegraph.models import SiteAvailability


@app.task
def update_site_availability_data() -> None:
    """
    This is a celery beat task which runs every second.
    Hits the allsafe.in url and saved result on database.
    """
    availability = requests.get("https://allsafe.in/", timeout=1)
    if availability.status_code == 200:
        is_uptime: bool = True
        status: int = 200
    else:
        is_uptime: bool = False
        status: int = 500
    SiteAvailability.objects.create(is_uptime=is_uptime, status=status)
    return None
