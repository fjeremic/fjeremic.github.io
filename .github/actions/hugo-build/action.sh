#!/bin/bash

cd ./themes/congo
npm install

cd ../../
npm run tailwind-build
npm run hugo-build
