python /srv/project/manage.py makemigrations --noinput
python /srv/project/manage.py migrate --noinput
python /srv/project/manage.py loaddata /srv/project/dump.json
python /srv/project/manage.py runserver 0.0.0.0:8081
