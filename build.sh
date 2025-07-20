#!/usr/bin/env bash
set -o errexit

pip install --upgrade pip
pip install -r pharmassit/requirements.txt

python pharmassit/manage.py collectstatic --no-input
python pharmassit/manage.py migrate
