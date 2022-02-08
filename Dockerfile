FROM python:3-alpine
LABEL maintainer="Asjad Jawed Siddiqui <asjadjawed@gmail.com>"

RUN apk add git jq yq bash

RUN addgroup -S asjad && adduser -S asjad -G asjad -s /bin/bash
USER asjad
WORKDIR /home/asjad/app

ENV PATH="/home/asjad/.local/bin:${PATH}"
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "src/main.py" ]
