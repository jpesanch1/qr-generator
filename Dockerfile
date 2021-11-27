FROM python@sha256:85d79ea7f22dd6eefb1101753129b5f681af7622c92f1e74f5cd58c18fb5dabd

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3" ]

CMD [ "qrcode-generator/generator.py" ]