FROM ubuntu:18.10

RUN apt-get update -y 
RUN apt-get install -y python3 python3-dev python3-pip
#RUN apt-get install flask


COPY  ./ ./timezone
WORKDIR ./app
ADD flasktime.py /app
ADD requirements.txt /app/
ADD templates/* /app/templates/
RUN pip3 install -r "requirements.txt"

EXPOSE 5000

CMD ["python3","flasktime.py"]


#FROM ubuntu:18.10
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
#COPY . /app
#WORKDIR /app
#RUN pip install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]

#ENTRYPOINT ["python3"]
#CMD [""]
