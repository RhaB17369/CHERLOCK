FROM python:3.8-alpine

LABEL maintainer="RhaB17369 <regonnebriceharold@gmail.com>"
LABEL dockerfile-creator="RhaB17369 <regonnebriceharold@gmail.com>"

RUN addgroup -S cherlock && \
    adduser -S cherlock -G cherlock

RUN apk add --no-cache gcc musl-dev libxml2-dev libxslt-dev nmap nmap-scripts openssl

USER raccoon
WORKDIR /home/cherlock
RUN pip install cherlock-scanner

ENV PATH=/home/raccoon/.local/bin:${PATH}

ENTRYPOINT ["cherlock"]
CMD ["--help"]
