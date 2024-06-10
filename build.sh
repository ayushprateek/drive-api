#!/bin/bash
#activate the virtual environment

source ./venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate

python3 manage.py loaddata fixtures/category.json