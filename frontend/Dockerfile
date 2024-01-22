# Use an official Node.js runtime as a parent image
FROM node:12-slim

# Set the working directory in the container
WORKDIR /frontend/src/app

COPY ./package.json ./

COPY package-lock.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
