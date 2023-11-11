FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    sudo \
    python3 \
    python3-pip \
    nodejs \
    npm \
    vim \
    net-tools \
    lsof
ENV newuser="mmouser"
RUN useradd -ms /bin/bash $newuser \
    && usermod -aG sudo $newuser \
    && echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER $newuser

WORKDIR /home/$newuser

RUN pip3 install eventlet python-socketio

COPY server.py .

#CMD ["tail", "-f", "/dev/null"]
CMD ["python3", "server.py"]