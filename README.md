First you should make venv for this project

python -m venv venv

Now you should activate your venv.

In Linux/macOS:

source venv/bin/activate    

In Windows:

venv/Scripts/activate.ps


pip install -r requirements.txt

Run the project

python manage.py runserver 8002


Now copy/paste this address in your browser URL bar:

http://127.0.0.1:8002/


Use The Project:
Now you should Login into the DjangoBlog

SuperUser role:

user:admin
password:1234


main admin panel path:
http://127.0.0.1:800/blog-django/