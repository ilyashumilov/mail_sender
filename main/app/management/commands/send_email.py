from django.core.management import BaseCommand
from app.tasks import email_sender
import pandas as pd

class Command(BaseCommand):
    def handle(self, *args, **options):
        data = pd.read_csv('main/app/data.csv')

        for index, row in data.iterrows():
            print(1)
            data = {
                'first_name': row['first_name'],
                'second_name': row['second_name'],
                'email': row['email'],
            }
            email_sender.s(data).apply_async(countdown=row['delay'])
