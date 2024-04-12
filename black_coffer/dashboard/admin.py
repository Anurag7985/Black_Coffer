# dashboard_app/admin.py

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import JsonData
from .resources import JsonDataResource

class JsonDataAdmin(ImportExportModelAdmin):
    resource_class = JsonDataResource
    list_display = ('intensity', 'likelihood', 'relevance', 'year', 'country', 'topics', 'region', 'city')
    search_fields = ('intensity', 'likelihood', 'relevance', 'year', 'country', 'topics', 'region', 'city')

admin.site.register(JsonData, JsonDataAdmin)
