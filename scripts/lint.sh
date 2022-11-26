#!/usr/bin/env bash

set -e
set -x

#mypy ecom
flake8 ecom tests
black ecom tests
#black ecom tests --check
isort ecom tests scripts
#isort ecom tests scripts --check-only