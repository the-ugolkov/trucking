FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py load_data uszips.csv
RUN python manage.py create_cars

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
