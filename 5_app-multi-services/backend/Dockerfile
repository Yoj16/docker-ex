FROM python:3.9
LABEL maintainer="Joy HEURTAUX"

WORKDIR /app

COPY ./app.py /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]