# Dockerfile
FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y postgresql-client
WORKDIR /simple

COPY requirements.txt /simple/
RUN pip3 install --no-cache-dir -r requirements.txt || { cat /simple/requirements.txt; exit 1; }

EXPOSE 8000
COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
