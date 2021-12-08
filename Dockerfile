FROM python:3-alpine

WORKDIR /home/robin/src/flask_app/cracked_flask

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","cracked_flask.py"]
