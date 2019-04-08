# A docker base image based on Alpine Linux with python 3.7.3 pre-installed
# Docker images can be stacked on top of each other.
FROM library/python:3.7.3-alpine

MAINTAINER Federico Mestrone

RUN mkdir /opt/myapp
RUN python3 -m venv venv

# Copy the webserver python app.
COPY app.py /opt/myapp
COPY requirements.txt /opt/myapp
COPY static /opt/myapp
COPY templates /opt/myapp

RUN cd /opt/myapp && pip3 install -r requirements.txt

# Set the default execution command for this image.
ENTRYPOINT cd /opt/myapp && export FLASK_APP=app.py && flask run --no-reload
