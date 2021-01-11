FROM python:3.7

RUN apt-get update

ARG project_dir=/src/

COPY requirements.txt $project_dir

WORKDIR $project_dir

RUN pip install -r requirements.txt