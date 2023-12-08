FROM python:3.9-slim
LABEL com.cuscuzmachine="wemyfelype@gmail.com"

ARG BUILD_DATE
ARG VCS_REF

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apt-get update -y && apt-get install alien git -y

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

ENV PORT=5000
EXPOSE 5000:5000

CMD [ "python", "API.py" ]