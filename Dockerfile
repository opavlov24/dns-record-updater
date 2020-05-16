FROM arm32v7/python:3.8.3-buster

COPY app /application/app
COPY requirements.txt /application
COPY main.py /application

RUN pip install --no-cache-dir -r ./application/requirements.txt

CMD [ "python", "./application/main.py" ]