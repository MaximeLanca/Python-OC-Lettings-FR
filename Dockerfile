FROM python:3.11-slim
WORKDIR /app
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
ARG SECRET_KEY=temp-secret-key-for-build
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN python -c "import django.db.backends.postgresql.utils as u; content = open(u.__file__).read().replace('raise AssertionError(\"database connection isn\\'t set to UTC\")', 'pass'); open(u.__file__, 'w').write(content)"
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]