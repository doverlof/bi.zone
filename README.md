# bi.zone
for future work

created by Filinov Dmitry

*** Описание подключения проекта для mac ***
1) скопируйте проект 
`git clone git@github.com:doverlof/bi.zone.git`
2) перейдите в проект 
`cd bi.zone`
`code .`
3) активируйте виртуальное окружение
`python -m venv .venv`
`source .venv/bin/activate`
4) перейдите в папку work, которая выше
`cd work`
5) выполните `docker-compose up --build`
6) зайдите в браузер по ссылке `http://localhost:8000`

*** Описание ссылок для выполнения заданий ***
По умолчанию перекидывает на страницу, на которой отобразятся все возможные действия.
1) посмотреть список всех добавленных подсетей `http://localhost:8000/subnet/`
2) создать подсеть `http://localhost:8000/create/` нужно будет ввести subnet и company_id
3) удалить подсеть по идентификатору `http://localhost:8000/delete/ID/` 
4) отфильтровать подсети, если параметры не заданы, то вывести все существующие
- по id `http://localhost:8000/filter/?id=ID`
- по company_id `http://localhost:8000/filter/?company_id=COMPANY_ID`
- по subnet `http://localhost:8000/filter/?subnet=SUBNET`
- по времени
    - после даты `http://localhost:8000/filter/?after_date=YYYY-MM-DDTHH:MM:SS`
    - до даты `http://localhost:8000/filter/?before_date=YYYY-MM-DDTHH:MM:SS`
    - в промежуток времени `http://localhost:8000/filter/?after_date=YYYY-MM-DDTHH:MM:SS&before_date=YYYY-MM-DDTHH:MM:SS`


