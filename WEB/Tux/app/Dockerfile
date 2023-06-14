FROM node:18-bullseye

WORKDIR /app
COPY package*.json ./

RUN apt update && apt upgrade
RUN apt install fortune cowsay -y

RUN npm install
COPY . .

ENV PATH $PATH:/usr/games
ENV PORT 3000

CMD [ "node", "src/index.js" ]