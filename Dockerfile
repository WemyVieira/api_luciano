FROM python:3.9-slim
LABEL com.cuscuzmachine="wemyfelype@gmail.com"

ARG BUILD_DATE
ARG VCS_REF

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=api.py

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]