FROM ubuntu:16.04
LABEL maintainer="Miguel Caballer <micafer1@upv.es>"
LABEL description="Container image to launch a jupyterhub server"

RUN apt update && apt install -y python3 python3-pip npm nodejs-legacy curl && \
    pip3 install jupyterhub && \
    pip3 install jupyter && \
    pip3 install jupyterhub-dummyauthenticator && \
    pip3 install jupyterhub-kubespawner && \
    npm install -g configurable-http-proxy && \
    apt remove -y npm python3-pip && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && rm -rf ~/.cache/

RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl && \
    chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

COPY jupyterhub_config.py /jupyterhub_config.py

ENV HUB_CONNECT_IP 127.0.0.1

EXPOSE 8000 8081

CMD jupyterhub --no-ssl
