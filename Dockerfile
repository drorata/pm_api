FROM python:3.6-slim-jessie

RUN apt-get update && apt-get install -y make git curl && mkdir -p /project/src

WORKDIR /project
COPY requirements.txt Makefile ./
RUN pip install -r requirements.txt

COPY src/ ./src
RUN make data && make train
ENTRYPOINT [ "python" ]
CMD [ "src/app.py" ]
