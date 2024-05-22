from django.core.management.base import BaseCommand
import pandas as pd
from scholarships.models import Scholarship, Degree, Tag
from datetime import datetime
import time
from django.core.files import File
from io import BytesIO
import requests
import os
from urllib.parse import urlparse

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('scholarshipsads.csv')
        for index, row in df.iterrows():
            response = requests.get(row['img'])
            name = row['name'].replace(" ", "_")  # Replace spaces with underscores
            file_name = f"{name}.jpg" 

            try:
                closing_date_str = row.get('closing-date')
                if pd.isna(closing_date_str) or closing_date_str == '':
                    closing_date = datetime.strptime('0001-01-01', '%Y-%m-%d').date()
                else:
                    closing_date = datetime.strptime(str(closing_date_str), '%Y-%m-%d').date()
            except ValueError:
                closing_date = datetime.strptime('0001-01-01', '%Y-%m-%d').date()

            
            
            scholarship = Scholarship.objects.create(
                name=row.get('name', ''),
                University_name=row.get('university', ''),
                # course=row.get('domains/2', ''),
                eligibity=row.get('open-to', ''),
                # tags=('open'),
                country=row.get('country', ''),
                closing_date=closing_date,
                funding_status=row['funding-status'],
                # degree=row['level'],
                subject=row['subjects'],
                degree=row['level']

            )
            scholarship.tags.set([12])
            scholarship.Scholarship_image.save(file_name, File(BytesIO(response.content)), save=True)
  

            # scholarship.degree.set(row['level'])



            self.stdout.write(self.style.SUCCESS(f'Successfully created: {row["name"]}'))

            # Introduce a delay to avoid rate limiting
            time.sleep(0.5)  # Sleep for 0.5 second


