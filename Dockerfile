# pull the official base image
FROM python:3.12.2-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies for creating virtual environment
#RUN apt-get python3-dev py-virtualenv
# RUN apk add py-virtualenv
RUN apt-get -y update && apt-get install -y python3-dev python3-venv

# Create virtual environment
RUN python3 -m venv venv

# Activate virtual environment
#RUN source venv/bin/activate
RUN bash -c "source venv/bin/activate"
# RUN apk add libpq-dev gcc \
#     && pip install psycopg2

RUN pip install wheel

#RUN apt-get install --virtual build-deps gcc python3-dev musl-dev \
 #  && apt-get install -y postgresql \
 #  && apt-get install -y postgresql-dev \
 #  && pip install psycopg2 \
 #  && apt-get install -y jpeg-dev zlib-dev libjpeg \
 #  && pip install Pillow \
 #  && apt-get autoremove --purge build-deps


# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# Install Nginx and dependencies
RUN apt-get install -y nginx
# copy project
COPY . /usr/src/app
COPY website/nginx.conf /etc/nginx/nginx.conf

# Install necessary tools (e.g., netcat)
#RUN apt-get netcat-busybox

EXPOSE 80

# Run Nginx in the foreground
CMD ["nginx", "-g", "daemon off;"]

RUN nginx -t
# Check if port 80 is listening
#RUN nc -z localhost 80
# Expose Nginx port and NodePort
#EXPOSE 80
EXPOSE 8000

ARG AWS_ACCESS_KEY_ID
ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID

ARG AWS_SECRET_ACCESS_KEY
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY

RUN python manage.py collectstatic -v 2 --noinput

RUN ls staticfiles
#RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate

#COPY run_migrations.sh /usr/src/app/run_migrations.sh
#RUN chmod +x /usr/src/app/run_migrations.sh
#RUN /usr/src/app/run_migrations.sh


#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# gunicorn --bind 0.0.0.0:8000 website.wsgi
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "website.wsgi:application"]

# Start Nginx and Gunicorn

#CMD ["nginx", "-g", "daemon off;"] & \
 #   gunicorn --bind 0.0.0.0:8000 website.wsgi:application

#ENTRYPOINT ["/app/run_migrations.sh", "&&", "gunicorn", "--bind", "0.0.0.0:8000", "website.wsgi:application"]

