# Django Project Instructions

## Project Stack



|  name          | version  |   |   |   |
|----------------|----------|---|---|---|
| python         |  3.12    |   |   |   |
| django         |  4.2.7   |   |   |   |
| elasticsearch  |          |   |   |   |
|                |          |   |   |   |





### elasticsearch Setup

download elasticsearch from: https://www.elastic.co/downloads/elasticsearch

after extracting go to bin file and open command promp.
for installing elasticsearch you can use bellow command.


```sh
elasticsearch.bat
```
now you can go to localhost:9200 and check your elasticsearch is active.

### Python Env Setup

Create a virtual environment to install dependencies inside it and activate it.

#### Virtualenv package

Create a virtual environment

```sh
python -m venv .venv
```

Activate virtual environment in linux

```sh
source .env/bin/activate
```

Activate virtual environment in windows

```sh
.\.env\Scripts\activate.bat
```

To install dependencies you can use bellow command.

```sh
pip install django
```

To save all dependencies version always after installation use bellow command.

```sh
pip freeze > requirements.txt
```
### Database Configuration

get random data from: https://newsapi.org/


### Essential packages for Elasticsearch

```sh
pip install django-elasticsearch-dsl
```

```sh
pip install django-elasticsearch-dsl-drf
```

### Prepare Settings

go to setting.py in your project and write bellow code for setting up elasticsearch.

```sh
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': 'http://localhost:9200',  
    },
}
```

### create index for data

for creating index for data in database you can use bellow command.

```sh
python manage.py search_index --rebuild
```

#### Run Project

You can now run the development server:

```sh
python manage.py runserver
```

Finally navigate to http://localhost:8000
