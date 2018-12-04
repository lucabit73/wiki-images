FROM python:3.6-alpine

ADD ./ /home/docker/application
# Default dir
WORKDIR /home/docker/application

RUN pip install -r requirements.txt

# Expose port
EXPOSE 8080

#CMD ["gunicorn", "app.wsgi", "-w", "7", "-t", "90", "-b", "0.0.0.0:8196"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
