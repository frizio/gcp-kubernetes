# A docker base image based on Debian 9 with python 3.7.3 pre-installed
FROM library/python:3.7.3-slim-stretch

# Meta-information about the image - some keys are commonly used, but anything can go here
LABEL maintainer="Federico Mestrone"
LABEL version="1.0"
LABEL description="A simple container for the GCP Developer Enablement Program"

# Create the Python virtual environment for our application
RUN mkdir /opt/myapp && \
    cd /opt/myapp && \
    python3 -m venv venv

# Install packages to support the Italian language
RUN apt-get update && \
    apt-get install -y locales locales-all
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# Copy the Python application itself and all files that go with it
COPY app.py /opt/myapp
COPY requirements.txt /opt/myapp
COPY static/ /opt/myapp/static
COPY templates/ /opt/myapp/templates

# Install the dependencies of our application using PIP
RUN cd /opt/myapp && \
    pip3 install -r requirements.txt

# Set the default execution command for our image
# This is the standard command used to run a Flask application
ENTRYPOINT cd /opt/myapp && \
           export FLASK_APP=app.py && \
           flask run --host 0.0.0.0 --no-reload
