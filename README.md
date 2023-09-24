# Lenta_project

### Опиание проекта
Проект в рамках хакатона Лента х Практикум сентябрь’23 на задаче:
Создание предсказательной модели и его интерфейса по прогнозированию спроса на товары заказчика собственного производства ООО “Лента”.

### Установка:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/Ivanmatv/Lenta_project.git
```
```
cd foodgram-project-react
```
Клонировать и установить виртуальное окружение:

- для MacOS
```
python3 -m venv venv
source venv/bin/activate
```
- для Windows
```
python -m venv venv
source venv/Scripts/activate
```
Установить зависимости:

```
cd backend
```
```
pip install -r requirements.txt
```

Применить миграции:
```
python manage.py makemigrations users
```
```
python manage.py makemigrations recipes
```

```
python manage.py migrate
```

***- В папке с файлом manage.py выполните команду для запуска локально:***

```
python manage.py runserver
```

Запустить все контейнера командой:
```
cd infra
```
```
docker-compose up -d --build
```

Выполнить миграции:

``` 
docker-compose exec backend python manage.py migrate 
```

Создайте суперпользователя:
```
docker-compose exec backend python manage.py createsuperuser
```

Загружаем статику:
```bash
docker-compose exec backend python manage.py collectstatic --no-input 
```

Наполните базу данных ингредиентами и тегами. Выполняйте команду из дериктории где находится файл manage.py:
```
python manage.py load_csv_data

```

Остановить работу всех контейнеров командой:
```
docker-compose down
```

### Примеры:


### Использумые технологии:

- Python - https://www.python.org/
- Django - https://www.djangoproject.com/
- Django Rest Framework - https://www.django-rest-framework.org/
- Docker - https://www.docker.com/
- Rest API - https://www.django-rest-framework.org/topics/documenting-your-api/

### Авторы проекта:

https://github.com/Ivanmatv - Иван Матвеев

