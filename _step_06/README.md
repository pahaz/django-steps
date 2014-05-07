# отделяем логику в отдельный апп #

* добавим поле в модель `created`/`updated`
* python manage.py schemamigration --auto complaints
* python manage.py migrate complaints
* создадим complaints/templates
* создадим complaints/urls.py
* улучшим админку


# способы переопределения поведения апликейшена и взаимодействия с app #

* templates
  * поиск шалона `TEMPLATE_LOADERS`, `TEMPLATE_DIRS`, поиск в `INSTALLED_APPS`

* custom views (собственнык url, добавление контекста во view)

* template_context_processors
  * рассказать про настройку `TEMPLATE_CONTEXT_PROCESSORS`

## http://djbook.ru/rel1.6/ref/templates/builtins.html#built-in-template-tags-and-filters ##
* template_tags
  * Регистрация фильтров
  * Потокобезопастность
  * `simple_tag`, `inclusion_tag`, `assignment_tag`

* переопределяем шаблоны в `_project_v6_/templates`

# цикл обработки запросов в Django #

* https://docs.djangoproject.com/en/dev/_images/middleware.svg
* показать римеры кода middleware из исходников django
