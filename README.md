# Проект асинхронного парсера документации Python

Асинхронный парсер документов PEP — Python Enhancement Proposal с официального сайта python.org.

## Информация об авторе
[Александр Лощилов](mailto:loshchilov.aleksandr@gmail.com?subject=[GitHub]%20PEP%20parser)

## Примененный стек технологий
Python, Scrapy

## Запуск проекта:
Склонирировать репозиторий удобным способом

Создать виртуальное окружение
```
python -m venv venv
```
Активировать виртуальное окружение

```
source venv/Scripts/activate
```

Установить зависимости
```
pip install -r requirements.txt
```

## Запуск парсера
Для парсинга запустить "паука" pep командой:
```
scrapy crawl pep
```

## Вывод результатов
Результаты парсинга сохраняются в папке 'results'

Cписок PEP сохраняется в файле с маской:
```
pep_%datetime%.csv
```

Сводка по статусам сохраняется в файле с маской:

```
status_summary_%datetime%.csv
```
