# milo-django

1. Clone GIT repo:
git clone https://github.com/lebvlad/milo-django.git
cd milo-django

2. Create and activate virtualenv:
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt

3. You can start with my 'db.sqlite' or delete it and generate new:
python3 manage.py makemigrations test_case
python3 manage.py migrate

Start server:
python3 manage.py runserver
