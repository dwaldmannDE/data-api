rm db.sqlite3
python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable
python manage.py loaddata seeds/station_seed.json
python manage.py initadmin