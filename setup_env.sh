#!/usr/bin/env bash

echo "installing serverless"
npm install -g serverless && \
    serverless plugin install -n serverless-python-requirements && \
    serverless plugin install -n serverless-offline

echo "installing python development dependencies"
pip install coverage pylint autopep8

echo "installing python application dependencies"
pip install -r requirements.txt