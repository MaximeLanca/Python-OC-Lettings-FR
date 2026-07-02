FROM python:3.11-slim
WORKDIR /app
ENV DJANGO_SETTINGS_MODULE=oc_lettings_site.settings
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000"]