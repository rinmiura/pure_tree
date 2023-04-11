from python:3.9

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./entrypoint.sh /entrypoint.sh
COPY ./config /config
WORKDIR /config
EXPOSE 8000

VOLUME ./config /config

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser user && \
    chown user:user -R /config && \
    chmod +x /config && \
    chown 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

ENV PATH="/py/bin:$PATH"

USER user
