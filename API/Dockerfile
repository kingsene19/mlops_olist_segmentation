FROM python:3.9-slim

WORKDIR /app/

ADD . /app/

RUN apt-get -y update
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000

CMD ["python", "app.py"]