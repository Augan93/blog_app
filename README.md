"# blog_app" 

## Инструкция по запуске

1.Создать бд в postgresql под именем "blogapp"

2. Создать новое окружение, активировать его и установить необходимые пакеты: pip install -r requirements.txt

3. python manage.py migrate

3. Создать юзера через python manage.py createsuperuser 

4. python manage.py runserver

5. Переходить по ссылке в браузере для инициализации данных в БД: 
http://localhost:8000/init_data/

6. http://localhost:8000/             - страница для получения постов

   http://localhost:8000/posts/new/   - страница для создания нового поста (требует авторизацию)
    