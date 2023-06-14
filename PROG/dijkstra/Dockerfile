FROM python:3

RUN apt-get update && apt-get install -y \
  xinetd \
  && rm -rf /var/lib/apt/lists/*

RUN mkdir /ctf
WORKDIR /ctf
RUN useradd -M -d /ctf ctf

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /ctf/

RUN chown -R root:ctf /ctf && \
  chmod -R 750 /ctf

RUN pip install -r /ctf/requirements.txt

# chown the matplotlib cache directory so that the ctf user can write to it
RUN chown -R ctf:ctf /root/.config/matplotlib

ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 40002