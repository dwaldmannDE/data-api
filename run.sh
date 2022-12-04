python manage.py migrate
python manage.py createcachetable
python manage.py loaddata seeds/station_seed.json
python manage.py initadmin
gunicorn --bind 0.0.0.0:8000 main.wsgi