FROM python:3.12.1

WORKDIR / grapher
COPY requirements.txt /grapher/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /grapher/requirements.txt

COPY . / grapher/

CMD bash -c "while true; do sleep 1; done"