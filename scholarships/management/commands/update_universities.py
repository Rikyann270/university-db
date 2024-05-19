

from django.core.management.base import BaseCommand
import pandas as pd
from scholarships.models import Universitie
import requests

from django.core.files import File
from io import BytesIO
import os
from urllib.parse import urlparse
import time  # Import time module for delay


class Command(BaseCommand):
    help = 'Import university data'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('all_universities.csv')
        for index, row in df.iterrows():
            university_url = row['web_pages/0']  # Assuming this contains the university website
            logo_url = "https://logo.clearbit.com/https://" + university_url

            # Download the image from the URL
            response = requests.get(logo_url)
            if response.status_code == 200:
                # Extract the university name and create a safe file name
                university_name = row['name'].replace(" ", "_")  # Replace spaces with underscores
                file_name = f"{university_name}.png"  # Use the university name with a .png extension

                # Create a Universitie object and save it
                universitie = Universitie.objects.create(
                    name=row['name'],
                    domain1=row.get('domains/0', ''),
                    domain2=row.get('domains/1', ''),
                    domain3=row.get('domains/2', ''),
                    domain4=row.get('domains/3', ''),
                    webpage1=row.get('web_pages/0', ''),
                    webpage2=row.get('web_pages/1', ''),
                    webpage3=row.get('web_pages/2', ''),
                    webpage4=row.get('web_pages/3', ''),
                    country=row['country'],
                    alpha_two_code=row['alpha_two_code'],
                    state_province=row['state-province']
                )

                # Save the image content to the University_image field
                universitie.University_image.save(file_name, File(BytesIO(response.content)), save=True)
                self.stdout.write(self.style.SUCCESS(f'Successfully created: {row["name"]}'))

                # Introduce a delay to avoid rate limiting
                time.sleep(1)  # Sleep for 1 second

            else:
                self.stdout.write(self.style.ERROR(f'Failed to download image for: {row["name"]}'))
