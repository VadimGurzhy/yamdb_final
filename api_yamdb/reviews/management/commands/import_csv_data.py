import csv
import os

from django.conf import settings
from django.core.management import BaseCommand
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User

FILE_NAME_MODEL = {
    'category.csv': Category,
    'genre.csv': Genre,
    'titles.csv': Title,
    'genre_title.csv': GenreTitle,
    'users.csv': User,
    'review.csv': Review,
    'comments.csv': Comment,
}

ALIAS_FOREIGN_KEY_FIELD = {
    'category': 'category_id',
    'author': 'author_id',
}


def read_csv_file(file_path):
    with (open(file_path, encoding='utf-8')) as file:
        csv_file_headers = next(csv.reader(file))
        headers = []
        for header in csv_file_headers:
            if header in ALIAS_FOREIGN_KEY_FIELD:
                headers.append(ALIAS_FOREIGN_KEY_FIELD[header])
            else:
                headers.append(header)
        return list(csv.DictReader(file, fieldnames=headers))


def load_csv(data, model, file_name):
    error_counter = 0
    for row in data:
        try:
            model.objects.create(**row)
        except Exception as error:
            error_counter += 1
            print(
                f'Ошибка при загрузке строки {row}'
                f'в модель {model.__qualname__}: {error}'
            )
    success_counter = len(data) - error_counter
    print(
        f'Файл {file_name} прочитан: {success_counter} из {len(data)}'
        f' строк записаны в базу. Ошибок: {error_counter}.'
    )


class Command(BaseCommand):

    def handle(self, *args, **options):
        for file_name, model in FILE_NAME_MODEL.items():
            file_path = os.path.join(settings.CSV_FILES_DIR, file_name)
            try:
                data = read_csv_file(file_path)
            except FileNotFoundError:
                print(f'Файл {file_path} не найден.')
            except Exception as error:
                print(f'Ошибка при чтении файла {file_name}: {error}')
            else:
                load_csv(data, model, file_name)
