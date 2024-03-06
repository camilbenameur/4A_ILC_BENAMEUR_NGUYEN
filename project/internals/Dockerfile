FROM python:3.8-slim

WORKDIR /srv/app

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "flaskr", "run", "--host", "0.0.0.0", "--debug"]
