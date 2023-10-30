FROM ubuntu:latest 

RUN apt-get update && apt-get install -y \
    sudo \
    python3 \
    vim \
    net-tools \
    lsof
ENV newuser="mmouser"
RUN useradd -ms /bin/bash $newuser \
    && usermod -aG sudo $newuser \
    && echo "%sudo ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER $newuser

WORKDIR /home/$newuser
COPY echo-server.py .

#CMD ["python3", "echo-server.py"]
CMD ["tail", "-f", "/dev/null"]