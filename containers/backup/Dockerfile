#!/bin/bash

ARG UBUNTU_VERSION=24.04
FROM ubuntu:${UBUNTU_VERSION}

ARG APP_VERSION=1.0.0
ENV APP_VERSION=${APP_VERSION}

WORKDIR /app
COPY backup .
RUN chmod +x backup

ENTRYPOINT ["./backup"]
CMD ["list"]
