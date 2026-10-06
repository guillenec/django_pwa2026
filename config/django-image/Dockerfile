FROM python:3.12-bookworm

RUN apt-get update && apt-get install libjpeg-dev graphviz graphviz-dev zlib1g-dev -y --force-yes && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]