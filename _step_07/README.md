# Примеры работы с моделями и менеджерами моделей #

* добавляем поля `publish_date`, `expiry_date`
* python manage.py schemamigration --auto complaints
* python manage.py migrate complaints

Показать как делать запросы к моделям.
* python manage.py shell  # https://docs.djangoproject.com/en/dev/topics/db/models/

Manager как единая точка запросов к данным.
(API ее используют, View ее используют, Tags ее используют).
Рассказать про менеджеры моделей.
Создание ModelManager и абстрактных моделей!

* пишем менеджер
* выносим логику в абстрактные модели

Изменяем view, templatetags: использование manager.

+ custom form template
