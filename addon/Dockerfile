ARG BUILD_FROM=homeassistant/amd64-base-python:3.9-slim
FROM $BUILD_FROM

RUN apk add --no-cache \
      bash \
      git \
      && pip install --no-cache-dir aiohttp==3.8.1

COPY run.sh /
COPY src/ /app/

RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
