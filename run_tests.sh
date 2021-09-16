#!/usr/bin/env bash

pylint ./src && \
    pylint ./tests && \
    coverage run -m unittest discover && \
    coverage report