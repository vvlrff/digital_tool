import csv

from django.core.management.base import BaseCommand, CommandError
from vacancy.models import Busyness


class Command(BaseCommand):
    help = 'Загружает типы занятости из csv-файла /data/busyness.csv'

    def handle(self, *args, **options):
        print('Uploading busyness to the database ... ', end='')
        try:
            with open('../data/busyness.csv') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    Busyness(
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
