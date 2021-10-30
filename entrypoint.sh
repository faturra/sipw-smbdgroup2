#----About APP----
# SMBD Group 2 SIPW (Sistem Informasi Pendaftaran Wisuda)
# Saturday, 09 October 2021 14.59
# https://www.faturrachmanmochammad.id
# V.1.0.0.0 20211023

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

gunicorn sipw.wsgi:application --bind 0.0.0.0:8110