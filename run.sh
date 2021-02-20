#!/bin/sh

gunicorn -b 0.0.0.0:5000 -w 4 src.articles.entrypoints.web_app:app

#gunicorn -b 0.0.0.0:5000 -w 4 simple:app