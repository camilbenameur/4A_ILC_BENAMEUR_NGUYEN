FROM python:3.8-slim

WORKDIR /srv/app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["flask", "--app", "./app", "run", "--host", "0.0.0.0", "--debug"]
