FROM python:3.12-slim

WORKDIR /app

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt /app

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py migrate

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]