FROM node:16-alpine as vueBuild
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY /312_vue/package.json /app/package.json
RUN npm install
COPY ./312_vue /app
RUN npm run build


FROM python:3.8

ENV HOME /root
WORKDIR /root

COPY . .
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait

# Download dependancies
RUN chmod +x /wait && pip3 install -r requirements.txt

COPY --from=vueBuild /app/dist ./static

EXPOSE 8080

CMD /wait && python server.py
#CMD python server.py