from django.core import management

from syndromic_tracker import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
