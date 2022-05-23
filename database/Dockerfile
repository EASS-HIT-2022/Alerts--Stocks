# docker build -t database . 
FROM python:3.7
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["python3", "db.py"]