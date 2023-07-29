FROM python:3.11.3-slim-buster
ENV LANG=C.UTF-8 TZ=Asia/Shanghai
ENV FLASK_APP service.py
ENV FLASK_RUN_HOST 0.0.0.0
WORKDIR /opt/dynamic_plugin_service
COPY . .

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
    && pip install --no-cache-dir pip -U \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo 'Asia/Shanghai' > /etc/timezone \
    && pip install -r requirements.txt

CMD ["flask", "run"]