web: gunicorn syndromic_tracker.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: celery worker --workdir backend --app=syndromic_tracker -B --loglevel=info
