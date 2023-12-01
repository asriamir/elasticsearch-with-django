from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from .models import *
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import(
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)

from .documents import *
from .serializers import *

def generate_random_data():
    url = 'https://newsapi.org/v2/everything?q=tesla&from=2023-10-03&sortBy=publishedAt&apiKey=5d287c6b61fb46c5988cf4c804f34c7e'
    r = requests.get(url)
    payload = json.loads(r.text)
    if 'articles' in payload:
        articles = payload['articles']
        count = 1
    # count = 1
        for data in payload.get('articles'):
            print(count)
            ElasticDemo.objects.create(
                title = data.get('title'),
                content = data.get('description') 
            )
            count += 1
    else:
        print("No articles found in the response.")
        
        
def index(request):
    generate_random_data()
    return JsonResponse({'status' : 200 })


class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    
    
    
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend
    ]
    
    search_fields = ('title', 'content')
    multi_match_search_fields = ('title' , 'content')
    filter_fields = {
        'title':'title',
        'content' : 'content',
    }