# This is a solution for my interview question for AllSafe company.

Problem Statement:
Create real-time charts/graphs with continuous job hitting the website allsafe.in for the status uptime/downtime?

Uptime - 200 status code
Downtime - 500 status code

The job will run every second interval hitting the website allsafe.in and store the data in a database with corresponding status code (200/500)

Build a chart or graph using the data stored in the database to plot and show the uptime and downtime of the website using Java/python and the graph/chart refreshes itself every second to show us the real-time status.

Project Setup Instruction:
Run pipenv install
Need following environment variables:
    SECRET_KEY
    DEBUG
    ALLOWED_HOSTS
    DB_HOST
    DB_USER
    DB_PASSWORD
    DB_NAME
    DB_PORT
    REDIS_URL (eg: redis://localhost:6379 for local)
    REDIS_CELERY_NAMESPACE (eg: 0)
    REDIS_APP_NAMESPACE (eg: allsafe)
