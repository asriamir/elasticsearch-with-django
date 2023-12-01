
from .models import ElasticDemo
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *

class NewsDocumentSerializer(DocumentSerializer):
    class Meta:
        model = ElasticDemo
        document = NewsDocument
        
        fields = ('title', 'content')
        
        
        def get_location(self , obj):
            try:
                return obj.location.to_dict()
            except:
                return {}








# class NewsDocumentSerializer(DocumentSerializer):
#     class Meta:
#         model = ElasticDemo
#         fields = ('title', 'content')
        
#     def get_location(self, obj):
#         try:
#             return obj.location.to_dict()
#         except:
#             return {}











# from .models import ElasticDemo
# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
# from .documents import NewsDocument  # Import the NewsDocument class from documents.py

# class NewsDocumentSerializer(DocumentSerializer):
#     class Meta:
#         model = ElasticDemo
#         document = NewsDocument  # Use the imported NewsDocument class here

#         fields = ('title', 'content')

#         def get_location(self, obj):
#             try:
#                 return obj.location.to_dict()
#             except:
#                 return {}
