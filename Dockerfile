FROM node:22-bookworm

# Setup Linux environment
RUN apt-get update && apt-get install -y curl python3 python3-venv

# Install Hugo specific version
ARG HUGO_VERSION="0.94.2"
RUN curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.deb" -o hugo.deb
RUN apt-get install ./hugo.deb

# Install python requirements for ./scripts
COPY requirements.txt /tmp/requirements.txt
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
RUN python3 -m pip install -r /tmp/requirements.txt
