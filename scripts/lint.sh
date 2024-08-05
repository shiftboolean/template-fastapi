#!/usr/bin/env bash

set -e
set -x

mypy app --ignore-missing-imports
ruff check app tests scripts
black app tests --check
