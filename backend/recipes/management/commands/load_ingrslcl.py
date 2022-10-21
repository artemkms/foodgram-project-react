import csv

from django.core.management import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Заполняет базу данных контентом из csv-файлов'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def import_ingredients(self, directory):
        with open(directory + 'ingredients.csv', 'r', encoding='UTF-8') as df:
            temp_data = []
            reader = csv.reader(df)
            for row in reader:
                temp_data.append(
                    Ingredient(
                        name=row[0],
                        measurement_unit=row[1],
                    )
                )
            Ingredient.objects.bulk_create(temp_data)

    def handle(self, *args, **options):
        directory = options['file_path']
        self.import_ingredients(directory)
