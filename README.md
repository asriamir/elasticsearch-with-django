
#readme in this link: https://github.com/asriamir/elasticsearch-with-django/tree/main/kernel#readme



# Elasticsearch with Django

This project demonstrates how to integrate **Django** with **Elasticsearch** for advanced search functionality. It fetches random news data from an external API, stores it in a Django model, and indexes it into Elasticsearch for real-time search capabilities.

## Features

- **Elasticsearch Integration**: Advanced search functionality using **Django Elasticsearch DSL**.
- **API Integration**: Fetches news data from [NewsAPI](https://newsapi.org/).
- **Django Admin**: Easily manage and view stored data via the Django admin panel.
- **Data Indexing**: Data is indexed into Elasticsearch for fast search.

## Requirements

- Python 3.x
- Django 3.x or higher
- Elasticsearch 7.x or higher

## Setup Instructions

### 1. **Elasticsearch Setup**
   - Download Elasticsearch from: [https://www.elastic.co/downloads/elasticsearch](https://www.elastic.co/downloads/elasticsearch).
   - After extracting, navigate to the `bin` directory and open a command prompt/terminal.
   - Run the following command to start Elasticsearch:
     ```
     elasticsearch.bat
     ```
   - Once Elasticsearch is running, you can verify it by visiting [http://localhost:9200](http://localhost:9200).

### 2. **Python Environment Setup**
   - Create and activate a virtual environment:
     ```
     python -m venv .venv
     ```
   - On Linux/Mac:
     ```
     source .venv/bin/activate
     ```
   - On Windows:
     ```
     .\.venv\Scriptsctivate.bat
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Save the installed dependencies to `requirements.txt`:
     ```
     pip freeze > requirements.txt
     ```

### 3. **Install Elasticsearch Dependencies**
   - Install necessary packages for Django and Elasticsearch:
     ```
     pip install django
     pip install django-elasticsearch-dsl
     pip install django-elasticsearch-dsl-drf
     ```

### 4. **Django Settings Configuration**
   - In your `settings.py`, add the following configuration to set up Elasticsearch:
     ```python
     ELASTICSEARCH_DSL = {
         'default': {
             'hosts': 'http://localhost:9200',  
         },
     }
     ```

### 5. **Create Index for Data**
   - Run the following command to create and rebuild the index for the data in the database:
     ```
     python manage.py search_index --rebuild
     ```

### 6. **Run the Project**
   - Start the Django development server:
     ```
     python manage.py runserver
     ```
   - Access the application at [http://localhost:8000](http://localhost:8000).

## API Endpoints

- **GET** `/` - Generates random news data and stores it in the database.
- **Search** - Use Elasticsearch to search for data based on the `title` and `content` fields.

## Admin Panel
You can manage the stored data through Django's admin panel. Access it at [http://localhost:8000/admin](http://localhost:8000/admin) (make sure to create a superuser if you haven't already).

## License
This project is open-source and available under the [MIT License](LICENSE).
