# pull the official base image
FROM python:3.13.0a3-alpine3.19

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies for creating virtual environment
RUN apk add python3-dev py-virtualenv
# RUN apk add py-virtualenv

# Create virtual environment
RUN python3 -m venv /opt/venv

# Activate virtual environment
RUN source /opt/venv/bin/activate

# RUN apk add libpq-dev gcc \
#     && pip install psycopg2

#RUN apk add python3.13-cgi
RUN pip install python3-cgi
RUN pip install wheel

RUN apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Install Nginx and dependencies
RUN apk add nginx

# copy project
COPY . /usr/src/app
COPY website/nginx.conf /etc/nginx/nginx.conf

RUN python manage.py collectstatic --noinput

# Expose Nginx port and NodePort
EXPOSE 80
EXPOSE 8000

RUN python manage.py migrate

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# gunicorn --bind 0.0.0.0:8000 website.wsgi
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "website.wsgi:application"]

# Start Nginx and Gunicorn
CMD ["nginx", "-g", "daemon off;"] & \
    gunicorn --bind 0.0.0.0:8000 website.wsgi:application

