FROM python:3.11

RUN pip install pipenv

WORKDIR /app

EXPOSE 8000

COPY Pipfile Pipfile.lock /app/

RUN pipenv install 

COPY . . 

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
