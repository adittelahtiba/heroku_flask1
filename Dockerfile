# FROM python:3.8.13-slim-buster
# WORKDIR /code
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# EXPOSE 5000
# COPY . .
# CMD ["flask", "run"]

FROM python:slim

WORKDIR /projects

RUN python3 -m venv venv
RUN . venv/bin/activate

# optimize image caching
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081
CMD [ "flask", "run", "--port=8081", "app:app"]