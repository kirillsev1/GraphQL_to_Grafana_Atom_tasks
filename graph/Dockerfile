FROM python


RUN mkdir -p /app/
WORKDIR /app/
COPY ./graph /app/
RUN pip install --upgrade pip

RUN pip install -r requirements.txt



CMD ["python","main.py"]
