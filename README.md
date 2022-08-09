# Урок 17. Домашнее задание - REST API на Flask.

В этом домашнем задании мы будем писать API для поиска фильмов с информацией об актерах, режиссерах и жанрах. У нашего API будут следующие эндпоинты:

- `/movies` — возвращает список всех фильмов, разделенный по страницам;
- `/movies/<id>` — возвращает подробную информацию о фильме.
- `/directors/` — возвращает всех режиссеров,
- `/directors/<id>` — возвращает подробную информацию о режиссере,
- `/genres/` —  возвращает всех режиссеров,
- `/genres/<id>` — возвращает информацию о жанре с перечислением списка фильмов по жанру,
- `POST /movies/` —  добавляет кино в фильмотеку,
- `PUT /movies/<id>` —  обновляет кино,
- `DELETE /movies/<id>` —  удаляет кино.

---

### Обязательное задание

### Шаг 1

Перейдите к репозиторию 17-го урока, где описаны модели и хранится база данных.

Изучите приложение и запустите его.

`Movie` **Модель фильма**

`id` — идентификатор

`title` — название фильма`description`  — описание фильма

`trailer` — трейлер 

`rating` — рейтинг

`genre` — ссылка на жанр

`director` — ссылка на режиссера

`Genre` **Жанр**

`id` — идентификатор

`name` — название жанра

`Director` **Режиссер**

`id` — идентификатор

`name` — имя режиссера

### Шаг 2

Напишите сериализацию модели `Movie`.
Установите Flask-RESTX, создайте CBV для обработки GET-запроса.

- `/movies` — возвращает список всех фильмов, разделенный по страницам;
- `/movies/<id>` — возвращает подробную информацию о фильме.

### Шаг 3

Доработайте представление так, чтобы оно возвращало только фильмы с определенным режиссером по запросу типа `/movies/?director_id=1`.

### Шаг 4

Доработайте представление так, чтобы оно возвращало только фильмы определенного жанра  по запросу типа `/movies/?genre_id=1`.

## Критерии приема ДЗ

- :white_check_mark:  Неймспейсы в RESTX использованы верно.
- :white_check_mark:  Методы GET для получения списка написаны верно.
- :white_check_mark:  Методы GET для получения записи написаны верно.
- :white_check_mark:  Методы POST написаны верно.
- :white_check_mark:  Методы DELETE написаны верно.
- :white_check_mark:  Обработка ошибок реализована верно.

## Задание со *звездочкой (необязательное)

### Шаг 1

Доработайте представление так, чтобы оно возвращало только фильмы с определенным режиссером и жанром по запросу типа `/movies/?director_id=2&genre_id=4`.

### Шаг 2

Добавьте реализацию методов `POST` для режиссера.

Добавьте реализацию методов `PUT` для режиссера.

Добавьте реализацию методов `DELETE` для режиссера.

### Шаг 3

Добавьте реализацию методов `POST` для жанра.

Добавьте реализацию методов `PUT` для жанра.

Добавьте реализацию методов `DELETE` для жанра.
