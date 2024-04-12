# dashboard_app/resources.py

from import_export import resources
from .models import JsonData

class JsonDataResource(resources.ModelResource):
    class Meta:
        model = JsonData
        fields = ('intensity', 'likelihood', 'relevance', 'year', 'country', 'topics', 'region', 'city')
        import_id_fields = ('intensity', 'likelihood', 'relevance', 'year', 'country', 'topics', 'region', 'city')
