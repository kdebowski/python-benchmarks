FROM python:3.7

ENV directory frameworks
ENV project aiohttp

COPY ./$directory/$project/. /app
COPY requirements.txt /app
WORKDIR ./app

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "run.sh"]