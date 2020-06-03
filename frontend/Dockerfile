FROM node:13-alpine as ui_builder

# Install dependencies
COPY package.json ./resume-ui/
WORKDIR /resume-ui
RUN npm install

# Build React application
COPY public ./public/
COPY src ./src/
COPY tsconfig.json ./
RUN npm run build

FROM nginx:alpine

#!/bin/sh

COPY nginx.conf /etc/nginx/nginx.conf

## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy from the stage 1
COPY --from=ui_builder /resume-ui/build /usr/share/nginx/html

EXPOSE 5000 5000

ENTRYPOINT ["nginx", "-g", "daemon off;"]

