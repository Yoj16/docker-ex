FROM nginx:alpine
LABEL maintainer="Joy HEURTAUX"

COPY dist /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/

VOLUME ["/usr/share/nginx/html/data", "/var/log/nginx", "/etc/nginx/conf.d"]

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]