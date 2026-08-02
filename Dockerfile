FROM nginx:alpine

COPY index.html /usr/share/nginx/html/index.html

COPY weather-icon.png /usr/share/nginx/html/weather-icon.png

COPY ngin.conf /etc/nginx/conf.d/default.conf

EXPOSE 80