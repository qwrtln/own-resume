FROM node:13-alpine as ui_builder

# Install dependencies
COPY frontend/package.json ./resume-ui/
WORKDIR /resume-ui
RUN npm install

# Build React application
COPY frontend/public ./public/
COPY frontend/src ./src/
COPY frontend/tsconfig.json ./
RUN ls && npm run build && ls

FROM nginx:alpine

#!/bin/sh

COPY nginx/nginx.conf /etc/nginx/nginx.conf

## Remove default nginx index page
RUN rm -rf /usr/share/nginx/html/*

# Copy from the stage 1
COPY --from=ui_builder /resume-ui/build /usr/share/nginx/html

EXPOSE 8888 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]

