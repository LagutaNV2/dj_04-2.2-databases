import json

from django.core.management.base import BaseCommand
from school.models import Teacher, Student


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('school.json', 'r', encoding="utf-8") as file:
            json_data = json.load(file)
            
        for row in json_data:
            print(f'{row=}')
            if row['model'] == "school.teacher":
                Teacher(
                    id = row['pk'],
                    name = row['fields']['name'],
                    subject = row['fields']['subject']
                ).save()
                
            if row['model'] == "school.student":
                Student(
                    id=row['pk'],
                    name=row['fields']['name'],
                    teacher_id=int(row['fields']['teacher']),
                    group=row['fields']['group']
                ).save()
                


