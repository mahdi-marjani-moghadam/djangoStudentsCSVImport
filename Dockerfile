FROM python:3.8.0b4-alpine3.10

COPY src/ src/  
COPY requirements.txt .

WORKDIR /src

ENV PATH="/py/bin:$PATH"

EXPOSE 8080

CMD ["./manage.py","runserver","0.0.0.0:8000"]
