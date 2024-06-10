### Drive AI Backend documentation

#### Getting Started

Project Setup [Installation Steps]

Install virtual environment

```

pip install virtualenv

```

create and activate the virtual env

```

python3 -m venv "venv_name"

source venv/bin/activate

```

Install requirements 

```
pip install -r requirements.txt
```

Migrate 

```

python manage.py migrate

```

Run Server

```

python manage.py runserver

```

Swagger API Documentation

```
{{base-URL}}/swagger/
Example: http://127.0.0.1:8000/swagger/
```

Redoc Documentation

```
{{base-URL}}/redoc/
Example: http://127.0.0.1:8000/redoc/
```