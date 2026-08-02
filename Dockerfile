FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

COPY weather-icon.png /usr/share/nginx/html/weather-icon.png