from django.core.management.base import BaseCommand
import pandas as pd
from courses.models import Subject

class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df = pd.read_csv('subjects_formatted.csv')
        for index, row in df.iterrows():
            subject_name = row['name']
            subject = Subject.objects.create(subject=subject_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created Subject: {subject}'))
