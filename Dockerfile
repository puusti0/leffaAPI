FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk update
RUN pip install -r requirements.txt --no-cache-dir

COPY . .

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]