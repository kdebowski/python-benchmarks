FROM python:3.7

ARG directory
ARG project

ENV env_directory=$directory
ENV env_project=$project

COPY /${env_directory}/${env_project}/. /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "run.sh"]