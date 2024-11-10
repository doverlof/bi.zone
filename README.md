# bi.zone
for future work

created by Filinov Dmitry

*** Описание подключения проекта ***
1) запускаем команду `python manage.py runserver`, по умолчани


*** Описание ссылок для выполнения заданий ***
По умолчанию перекидывает на страницу, на которой отобразятся все возможные действия.
1) посмотреть список всех добавленных подсетей `http://127.0.0.1:8000/subnet/`
2) создать подсеть `http://127.0.0.1:8000/create/` нужно будет ввести subnet и company_id
3) удалить подсеть по идентификатору `http://127.0.0.1:8000/delete/ID/` 
4) отфильтровать подсети, если параметры не заданы, то вывести все существующие
- по id `http://127.0.0.1:8000/filter/?id=ID`
- по company_id `http://127.0.0.1:8000/filter/?company_id=COMPANY_ID`
- по subnet `http://127.0.0.1:8000/filter/?subnet=SUBNET`
- по времени
    - после даты `http://127.0.0.1:8000/filter/?after_date=YYYY-MM-DDTHH:MM:SS`
    - до даты `http://127.0.0.1:8000/filter/?before_date=YYYY-MM-DDTHH:MM:SS`
    - в промежуток времени `http://127.0.0.1:8000/filter/?after_date=YYYY-MM-DDTHH:MM:SS&before_date=YYYY-MM-DDTHH:MM:SS`


