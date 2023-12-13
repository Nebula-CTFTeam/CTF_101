FROM ubuntu:22.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd python3

RUN useradd -m ctf

WORKDIR /home/ctf

COPY ./flag /flag
COPY ./httpd /home/ctf/httpd
COPY ./resources /home/ctf/resources
RUN echo "You are blocked currently. Please try again later." > /etc/banner_fail

RUN chmod +x /home/ctf/httpd && \
    chown -R ctf:ctf /home/ctf/

CMD ["/home/ctf/httpd"]

ENV LISTEN_PORT 31337
