FROM python:3.7
ENV PYTHONPATH=/code
ARG REQ_HASH=latest
MAINTAINER ddmitiy
RUN mkdir /code
RUN mkdir /code/back
ADD ./back /code/back
WORKDIR /code/back
RUN pip install --no-cache-dir pipenv && pipenv install
ENV PORT=5632
CMD python -m pipenv run python main.py
