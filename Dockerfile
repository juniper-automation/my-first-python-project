FROM python:3.8-bullseye

### -------------------------------------------------
### Metadata information
### -------------------------------------------------
LABEL name="my-first-python-project"
LABEL maintainer="cremsburg@protonmail.com"
LABEL description="python container to download configurations"
LABEL license="GPLv3"
LABEL url="https://gitlab.com/calvinr-containers/my-first-python-project/container_registry"
LABEL build-date="20210826"

### -------------------------------------------------
### Environmentals
### -------------------------------------------------
ENV POETRY_VERSION 1.1.7
ENV PYTHONUNBUFFERED 1

### -------------------------------------------------
### Setup Python tooling
### -------------------------------------------------
RUN apt update && apt install gcc

### -------------------------------------------------
### Install Poetry to help with dependency management
### -------------------------------------------------
RUN pip install --upgrade pip
RUN pip install wheel
RUN pip install poetry==$POETRY_VERSION

### -------------------------------------------------
### Caching dependencies
### -------------------------------------------------
WORKDIR /home/python
COPY poetry.lock pyproject.toml /home/python/

### -------------------------------------------------
### Disable virtualenv
### -------------------------------------------------
RUN poetry config virtualenvs.create false 
RUN poetry install --no-interaction --no-ansi

# Creating folders, and files for a project:
COPY app.py /home/python
COPY .env /home/python
