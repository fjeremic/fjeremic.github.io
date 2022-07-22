# jeremic.ca

Personal website of Filip Jeremic. Statically built using [Hugo](https://gohugo.io/) and
[congo](https://git.io/hugo-congo). Deployed using [GitHub Actions](https://github.com/features/actions) and
[GitHub Pages](https://pages.github.com/) in a Dockerized environment.

## Docker

The Dockerfile in the root of the repository builds a docker image with the exact dependencies needed to generate the
static website. The GitHub Actions automation which builds and deploys the website is built using the same docker image.

### Setup

We first build the docker image:

```
docker build . -t jeremic.ca
```

Next we initialize the git submodule which will clone the Hugo theme:

```
git submodule init
git submodule update
```

Next we need to install the theme dependencies by mounting the current repository inside the docker container:

```
docker run -v $PWD:/$PWD -w $PWD/themes/congo -it jeremic.ca npm install
```

### Build

To build the site we need to first invoke the Tailwind CSS JIT compiler to parse the website and theme contents and
generate the CSS file from a union set of all CSS classes used. Following the CSS generation we invoke the Hugo build
system to generate the static website.

We can use the same script that is used by the automation to accomplish this:

```
docker run -v $PWD:/$PWD -w $PWD -it jeremic.ca .github/actions/hugo-build/action.sh
```

Alternatively we can manually invoke the two steps:

```
docker run -v $PWD:/$PWD -w $PWD -it jeremic.ca npm run tailwind-build
docker run -v $PWD:/$PWD -w $PWD -it jeremic.ca npm run hugo-build
```

The static website is generated in the `./public` directory.

### Watch

When making changes to the website it is inconvenient to have to build and serve the website after each change. Instead
we can launch two processes in our docker container which will watch for any changes to our website and automatically
rebuild and serve the content. We can use two terminal shells to invoke the following two commands:

```
docker run -v $PWD:/$PWD -w $PWD -it jeremic.ca npm run tailwind-watch
docker run -v $PWD:/$PWD -w $PWD -p 8000:8000 -it jeremic.ca npm run hugo-watch
```

## LaTeX

We purposely don't install the Linux LaTex packages in the Dockerfile because it bloats the image size unnecessarily.
We can install the LaTex packages manually and build the Resume inside the docker container as follows:

```
# Run the docker container as an interactive shell
docker run -v $PWD:/$PWD -w $PWD -it jeremic.ca /bin/bash

# Install LaTeX
apt-get install -y texlive texstudio

# Build the Resume
pdflatex Filip-Jeremic-Resume.tex
```
