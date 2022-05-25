FROM python:3.8-slim-buster

WORKDIR '/app'


RUN pip install pygame
RUN apt update
RUN apt-get install -y libglib2.0-0 libsm6 libxrender1 libxext6 libasound2
#RUN apt-get install libasound2:i386
COPY . .

EXPOSE 5555

CMD [ "python3", "./menu.py"]