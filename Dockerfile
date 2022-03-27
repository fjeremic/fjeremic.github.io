FROM node:17.7.2

# Setup Linux environment
RUN apt-get update
RUN apt-get install -y curl python3 python3-pip
RUN dpkg --add-architecture amd64
RUN apt-get update

# Install Hugo specific version
ARG HUGO_VERSION="0.94.2"
RUN curl -L "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_Linux-64bit.deb" -o hugo.deb
RUN apt-get install ./hugo.deb

# For GitHub Action type workflow we'll create a copy of the repository inside the image. For development we typically
# want to mount the respoitory from the host into the container so that any changes made on the host are reflected
# instantly inside the container. The volume mount takes precedence over the copy.
COPY . /website

WORKDIR /website

# Install python requirements for ./scripts
RUN python3 -m pip install -r requirements.txt
