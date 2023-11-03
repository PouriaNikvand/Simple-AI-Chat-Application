FROM python:3.11

# File Author / Maintainer
MAINTAINER Pouria.Nikvand

RUN pip install --upgrade pip
RUN apt-get clean
RUN apt-get update
#RUN apt-get install -y --no-install-recommends build-essential telnet
#RUN apt-get install -y --no-install-recommends curl net-tools libssl-dev
#RUN apt-get install -y --no-install-recommends vim htop unzip wget

RUN mkdir /app

COPY requirements.txt /app
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY src /app/src
COPY app.py /app/
COPY configs/config.yml /app/
COPY configs/production.yml /app/

WORKDIR /app/
ENV PYTHONPATH="/app/"
EXPOSE 8585

# Start processes
CMD ["python", "app.py", "-c", "production.yml"]

# Running the container without any specific app
#CMD ["tail", "-f","/dev/null"]