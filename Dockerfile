FROM node:8 as builder
WORKDIR /usr/src/app
COPY package*.json ./
ENV NODE_ENV=production
RUN npm install --production
COPY . .


FROM arm32v7/node
WORKDIR /usr/src/app
COPY --from=builder /usr/src/app .
CMD [ "npm", "start" ]


