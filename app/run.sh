#!/bin/sh

exec pipenv run gunicorn -b :5999 --access-logfile -e SCRIPT_NAME=/something app:app
