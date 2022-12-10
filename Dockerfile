FROM harbor.kube.itdw.io/docker/library/python:3.11-slim-bullseye

EXPOSE 8080

WORKDIR /code

COPY requirements.txt /code/requirements.txt

COPY . /code

RUN apt install -y grep && pip install --upgrade pip && pip install --no-cache-dir -r /code/requirements.txt

RUN chmod +x run.sh

CMD /code/run.sh
