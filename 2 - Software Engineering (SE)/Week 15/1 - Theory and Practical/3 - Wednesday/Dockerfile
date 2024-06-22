FROM python:3.8

WORKDIR /flask_app

COPY app.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "./app.py" ]