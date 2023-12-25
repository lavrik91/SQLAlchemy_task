FROM python:3.10

RUN pip install --upgrade pip

WORKDIR /app

RUN pip install --no-cache-dir psycopg2-binary

COPY poetry.lock pyproject.toml /app/


RUN pip install poetry

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . .

RUN chmod a+x docker/*.sh

# WORKDIR src
# CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
# # CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]