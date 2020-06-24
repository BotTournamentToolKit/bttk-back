FROM ubuntu:16.04

# install python 3.7 and pip.
RUN apt-get update
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update
RUN apt-get install python3-pip -y
RUN apt-get install python3.7 -y

# copy app files
COPY requirements.txt /usr/src/app/

# install dependencies
RUN python3.7 -m pip install --upgrade pip
RUN python3.7 -m pip install --no-cache-dir -r /usr/src/app/requirements.txt


# expose ports
EXPOSE 8000

# start app
CMD ["python3.7", "/usr/src/app/launch.py"]