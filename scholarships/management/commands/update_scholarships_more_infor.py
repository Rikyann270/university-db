from django.core.management.base import BaseCommand
import pandas as pd
from scholarships.models import Scholarship

class Command(BaseCommand):
    help = 'Update existing scholarships'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('more scholership infor.csv')

        for index, row in df.iterrows():
            # Attempt to find the scholarship by name
            scholarship = Scholarship.objects.filter(name=row.get('n-name', '')).first()

            if scholarship:
                # Update existing scholarship fields
                scholarship.description = row.get('n-description', '')
                scholarship.degree_level = row.get('n-degree-level', '')
                scholarship.available_subjects = row.get('n-availability-subject', '')
                scholarship.eligible_criteria = row.get('n-eligibility-criteria', '')
                scholarship.eligible_nationality = row.get('n-eligibility', '')
                scholarship.benefits = row.get('n-benefit', '')
                scholarship.application = row.get('n-application', '')
                scholarship.application_link = row.get('n-application-link', '')
                scholarship.save()
                
                self.stdout.write(self.style.SUCCESS(f'Successfully updated: {row["n-name"]}'))
            else:
                self.stdout.write(self.style.WARNING(f'No match found for: {row["n-name"]}'))
