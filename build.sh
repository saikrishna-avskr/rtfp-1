#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r pharmassit/requirements.txt
python pharmassit/manage.py migrate
python pharmassit/manage.py collectstatic --no-input
