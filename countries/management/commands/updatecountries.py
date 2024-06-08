from django.core.management.base import BaseCommand
import pandas as pd
from countries.models import Country_details

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('countrycode.csv')
        for index, row in df.iterrows():
            country = Country_details.objects.create(
                country_name = row['country-col'],
                country_code = row['country_codee'],
                phone_code = row['phone_codee']
                )
        self.stdout.write(self.style.SUCCESS(f'Successfully created: {row['country-col']}'))
