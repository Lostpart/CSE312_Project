FROM python:3.8

ENV HOME /root
WORKDIR /root

COPY . .
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait

# Download dependancies
RUN chmod +x /wait && pip3 install -r requirements.txt
# RUN pip3 install -r requirements.txt

EXPOSE 8080

CMD /wait && python server.py
#CMD python server.py