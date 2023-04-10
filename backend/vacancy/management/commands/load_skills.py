import csv

from django.core.management.base import BaseCommand, CommandError
from vacancy.models import Skills


class Command(BaseCommand):
    help = 'Загружает навыки из csv-файла /data/skills.csv'

    def handle(self, *args, **options):
        print('Uploading ingredients to the database ... ', end='')
        try:
            with open('../data/skills.csv') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    Skills(
                        name=row[0],
                    ).save()
                print('Done')
        except FileNotFoundError:
            raise CommandError("Can't open file")
        except (IndexError, AttributeError):
            raise CommandError('Data entry error')
        except PermissionError:
            raise CommandError('File access error')
        except OSError:
            raise CommandError('File system error')
