FROM python:3.8.3-alpine
RUN mkdir /code
# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add  gettext
# install psycopg2 dependencies
#RUN apk update \
#    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk update \
    && apk add --no-cache --virtual .build-deps \
    ca-certificates gcc python3-dev postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

#RUN apk add  gettext  msgfmt  msgmerge   msguniq


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install pillow

RUN pip install django-developer-panel && pip install django-seed

# copy project
COPY . /code/