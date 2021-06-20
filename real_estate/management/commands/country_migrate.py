import json
from django.core.management.base import BaseCommand
from real_estate.models import Country

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)

        for data in data_list:
            data['pk'] = data.pop('alpha2Code')
            Country.objects.get_or_create(pk=data['pk'], defaults=data)
