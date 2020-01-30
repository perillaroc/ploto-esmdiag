FROM nwpc-oper/ploto-esmdiag:base

LABEL maintainer="perilalroc@gmail.com"

USER hujk

WORKDIR /srv/run

COPY ploto_esmdiag/ /srv/ploto-esmdiag/ploto_esmdiag
COPY setup.py /srv/ploto-esmdiag/setup.py
COPY vendor/ /srv/vendor

SHELL ["conda", "run", "-n", "ncl_stable", "/bin/bash", "-c"]

RUN cd /srv/ploto \
    && python3 -m pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple \
    && python3 -m pip install . \
    && cd /srv/ploto-esmdiag \
    && python3 -m pip install .

ENTRYPOINT ["python3", "/srv/ploto/ploto/scheduler/rabbitmq/consumer/consumer.py"]

ENV ESMDIAG_ROOT=/srv/vendor/esmdiag

CMD ["--config-file=/etc/ploto/consumer.config.yaml"]