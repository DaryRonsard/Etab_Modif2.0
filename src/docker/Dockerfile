FROM python:3.11-slim-buster

WORKDIR /MonEtab

COPY requirements.txt .

#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



#FROM ubuntu:latest
#LABEL authors="RonsardHien"
#
#ENTRYPOINT ["top", "-b"]
