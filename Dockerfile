FROM python:3.11

COPY . /items_registration_api
WORKDIR /items_registration_api
RUN pip install -r requirements.txt
RUN python manage.py migrate