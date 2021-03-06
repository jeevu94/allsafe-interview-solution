# This is a solution for my interview question for AllSafe company.

**Problem Statement**:
Create real-time charts/graphs with continuous job hitting the website allsafe.in for the status uptime/downtime?

Uptime - 200 status code
Downtime - 500 status code

The job will run every second interval hitting the website allsafe.in and store the data in a database with corresponding status code (200/500)

Build a chart or graph using the data stored in the database to plot and show the uptime and downtime of the website using Java/python and the graph/chart refreshes itself every second to show us the real-time status.

**Project Setup Instructions:** </br>
1. Run pipenv install </br>
2. Need following environment variables in .env file
- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DB_HOST
- DB_USER
- DB_PASSWORD
- DB_NAME
- DB_PORT
- REDIS_URL (eg: redis://localhost:6379 for local)
- REDIS_CELERY_NAMESPACE (eg: 0)
- REDIS_APP_NAMESPACE (eg: allsafe)
3. Runserver
4. Run celery worker `celery -A allsafe worker --pool=solo -l info` for windows or just `celery -A worker worker -l info`
5. Run celery beat `celery -A allsafe beat -l info`

Example of final result: </br>
Each bar is a second and 20 most recent seconds are displayed at every new second. 
<img src="assets/images/availability.jpg">
