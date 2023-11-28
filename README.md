## Описание
Byte of Python Bot — телеграм-бот шпаргалка, который поможет освежить знания языка Python. 

Создан на базе текста свободной книги «A Byte of Python», которая может служить учебным пособием или руководством по языку Python для начинающей аудитории.

Оргинальный перевод книги был дополнительно адаптирован и сконверирован в формат .txt.

Работающая версия: https://t.me/byte_of_python_bot

## Технологии
* Python 3.11,
* aiogram 3.x (фреймворк для создания ТГ-ботов),
* loguru (библиотека для логирования).

## Установка и запуск
Для установки зависимостей используйте `poetry`.

Перед запуском бота нужно переименовать файл .env.example в .env, и указать в .env:
* токен вашего ТГ-бота.