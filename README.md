https://github.com/VadimGurzhy/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg
# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VadimGurzhy/infra_sp2.git
```

```
cd infra_sp2
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```


```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Переходим в папку с файлом docker-compose.yaml:

```
cd infra
```

Поднимаем контейнеры:

```
docker-compose up -d --build
```
Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:

```
docker-compose exec web python manage.py createsuperuser:
```

Собираем статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Останавливаем контейнеры:

```
docker-compose down -v
```

# Описание:

Бэкенд учебного группового проекта YaMDb для взаимодействия по API.  
Проект собирает отзывы пользователей на произведения (книги, фильмы, музыка). Возможности:
* Загрузка базы проекта из внешних файлов (csv).
* Регистрация пользователей с подтверждением через e-mail.
* Разграничение прав пользователей - администратор, модератор и пользователь.
* Зарегистрированные пользователи могут оставлять отзывы с оценкой произведения, а также комментарии к отзывам.
* Формирование рейтинга произведений по оценкам пользователей.

После запуска проекта полную документацию API с примерами можно найти по ссылке:  
<http://127.0.0.1:8000/redoc/>

# Как загрузить базу проекта из внешних файлов
Папка хранения файлов .csv определяется в переменной CSV_FILES_DIR в settings.py. По умолчанию - 'static/data'.

Для загрузки файлов нужно выполнить следующую команду:
```
python3 manage.py import_csv_data
```

# Примеры запросов:
 
 ## Регистрация нового пользователя


```
POST /api/v1/auth/signup/
```
Параметры тела запроса:
| Имя     | Тип       | Описание                           |
|---------|-----------|------------------------------------|
| username | string | Имя пользователя |
| email | string \<email> | Email |

Пример успешного ответа:
```
{
  "email": "string",
  "username": "string"
}
```
## Получение JWT-токена
```
POST /api/v1/auth/token/
```
Параметры тела запроса:
| Имя     | Тип       | Описание                           |
|---------|-----------|------------------------------------|
| username | string | Имя пользователя |
| confirmation_code | string | Код подтверждения |

Пример успешного ответа:
```
{
"token": "string"
}
```

## Получение списка всех произведений
```
GET /api/v1/titles/
```

Параметры запроса:
| Имя     | Тип       | Описание                           |
|---------|-----------|------------------------------------|
| category | string | **опционально** <p> Категория </p>|
| genre | string | **опционально** <p> Жанр </p>|
| name | string | **опционально** <p> Название произведения </p>|
| year | integer | **опционально** <p> Год выпуска </p>|

Пример успешного ответа:
```
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```

## Добавление нового отзыва
```
POST /api/v1/{title_id}/reviews/
```
Параметры запроса
| Имя     | Тип       | Описание                           |
|---------|-----------|------------------------------------|
| title_id | integer | ID произведения|

Параметры тела запроса:
| Имя     | Тип       | Описание                           |
|---------|-----------|------------------------------------|
| text | string | Текст отзыва|
| score | integer [1..10] | Оценка |

Пример успешного ответа:
```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "score": 1,
  "pub_date": "2019-08-24T14:15:22Z"
}
```

## Получение комментария к отзыву
``` 
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```
Параметры запроса
| Имя     | Тип       | Описание                           |
|---------|-----------|------------------------------------|
| title_id | integer | ID произведения|
| review_id | integer | ID отзыва|
| comment_id | integer | ID комментария|


Пример успешного ответа:
```
{
"id": 0,
"text": "string",
"author": "string",
"pub_date": "2019-08-24T14:15:22Z"
}
```

# Использованные технологии:

* [python](https://www.python.org/doc/)
* [django](https://docs.djangoproject.com/en/3.2/)
* [django-rest-framework](https://www.django-rest-framework.org/)
* [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)

# Авторы:

* [Мамед Алибеков](https://github.com/Niechec) (Регистрация и аутентификация, пользователи)
* [Вадим Гуржий](https://github.com/VadimGurzhy) (Произведения, категории, жанры, импорт данных из csv)
* [Алексей Ким](https://github.com/kim-a-s) (Отзывы, комментарии, рейтинги)