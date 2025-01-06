import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MisakaMikoto_project.settings')
# configure the settings for the project

import django
django.setup()

# Fake population script
import random
from MisakaMikotoApp1.models import MisakaMikoto, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()

def add_person():
    """Creates or retrieves a MisakaMikoto entry with unique email."""
    fake_name = fakegen.name()
    fake_age = fakegen.random_int(min=18, max=80)
    fake_email = fakegen.unique.email()

    person = MisakaMikoto.objects.get_or_create(name=fake_name, age=fake_age, email=fake_email)[0]
    return person

def populate(N=5):
    for _ in range(N):
        # Get or create a person (topic in this context)
        person = add_person()

        # Create fake data for the webpage
        fake_url = fakegen.url()
        fake_name = fakegen.company()

        # Create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=person, url=fake_url, name=fake_name)[0]

        # Create a fake access record for that webpage
        fake_date = fakegen.date()
        AccessRecord.objects.get_or_create(name=webpg, date=fake_date)

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Populating complete!")
