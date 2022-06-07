FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential netcat \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # Additional dependencies
  && apt-get install -y procps telnet \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*


# Requirements are installed here to ensure they will be cached.
COPY ./Pipfile* /
RUN pip install pipenv \
    && pipenv install --deploy --system

COPY ./compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint \
    && chmod +x /entrypoint

COPY ./compose/start /start
RUN sed -i 's/\r$//g' /start \
    && chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]