#!/bin/sh

nohup /home/pi/berryconda3/envs/django/bin/python manage.py runserver 0.0.0.0:8000 > server.log 2>&1 &
