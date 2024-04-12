# dashboard_app/management/commands/import_json.py

import json
from django.core.management.base import BaseCommand
from dashboard.models import JsonData

class Command(BaseCommand):
    help = 'Import JSON data into the database'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str, help='Path to the JSON file to import')

    def handle(self, *args, **kwargs):
        file_path = '/root/blackCoffer/black_coffer/jsondata.json'
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                for item in data:
                    JsonData.objects.create(
                        intensity=item['intensity'],
                        likelihood=item['likelihood'],
                        relevance=item['relevance'],
                        year=item['year'],
                        country=item['country'],
                        topics=item['topics'],
                        region=item['region'],
                        city=item['city']
                    )
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {file_path}'))
