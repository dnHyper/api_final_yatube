
# Яндекс.Практикум. Спринт 9

#### Название: Проект «API для Yatube»
#### Папка: api_final_yatube
#### Группа: когорта 25
#### Когда: 2022 год
#### Кто: Алексей Ерёменко ( https://github.com/dnHyper/ )

------------

## Вместо вступления:
Если вы проходите обучение по курсу Яндекс.Практикум Python-разработчик, и должны выполнить финальный проект очередного спринта, то … рекомендую подсматривать выложенный мной код лишь *в крайнем случае*. Лично я, во время написания данного кода, использую исключительно подсказки ревьюера, поисковик и документацию по python & django, советую и вам поступать таким же образом.

------------

# Описание:
Продолжение обучения, в этот раз для над начатой в третьем спринте, [социальной сети](https://github.com/dnHyper/hw02_community), добавляем api. В рамках данного спринта было добавлено:

- Выдача по api постов с пагинацией
- Выдача по api групп с пагинацией
- Выдача по api подписок
- Выдача по api комментариев
- Разграничение прав:
- - Можно редактировать/удалять только свои записи
- - Гости могут только смотреть записи


## Запуск проекта

Создайте и активируйте виртуальное окружение (для *nix/MacOS):

    python3 -m venv venv
    source venv/bin/activate

Установие зависимости из файла requirements.txt:

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

Выполните миграции:

    python3 manage.py migrate


Запустите проект

    python3 manage.py runserver

## Возможные проблемы

На данный момент никаких проблем при разворачивании приложения быть не должно. Стоит только учитывать, что база данных создаётся пустой, потому стоит перед началом работы минимально наполнить её, добавив хотя-бы одну запись. Для добавления групп используйте инструменты для работы с БД (через API добавлять группы нельзя).

## Лицензия
[MIT](https://ru.wikipedia.org/wiki/%D0%9B%D0%B8%D1%86%D0%B5%D0%BD%D0%B7%D0%B8%D1%8F_MIT)


