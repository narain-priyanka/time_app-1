FROM python:3.11.2-alpine3.17

# Set up a working folder and install the pre-reqs
RUN mkdir -p /home/app

RUN pip install --upgrade pip
RUN pip install Flask
RUN pip install pytz

COPY . /home/app

CMD [ "python", "./home/app/run.py" ]
