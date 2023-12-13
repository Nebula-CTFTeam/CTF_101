FROM ubuntu:22.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd python3

RUN useradd -m ctf

WORKDIR /home/ctf

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
COPY ./flag /flag
COPY ./nebudbg /home/ctf/nebudbg
RUN echo "You are blocked currently. Please try again later." > /etc/banner_fail

RUN chmod +x /start.sh && \
    chmod +x /home/ctf/nebudbg && \
    chown -R ctf:ctf /home/ctf/

CMD ["/start.sh"]

ENV LISTEN_PORT 31337
