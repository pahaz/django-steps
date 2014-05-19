# добавляем модель пользователи, регистрация, права пользователей, группы #

 * Делаем собственную модель пользователя в `customauth`.
https://docs.djangoproject.com/en/dev/topics/auth/customizing/#a-full-example - пример
User: qw@qw.qq:qwer
AUTH_USER_MODEL = 'customauth.User'

 * Комментировать могут только зарегистрированные пользователи.

# (next) ContentType - generic комменты #
