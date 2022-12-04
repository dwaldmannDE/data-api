python manage.py migrate
python manage.py loaddata seeds/station_seed.json
python manage.py createcachetable
gunicorn --bind 0.0.0.0:8000 main.wsgi