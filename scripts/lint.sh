#!/usr/bin/env bash

set -e
set -x

mypy app --ignore-missing-imports
ruff app tests scripts
black app tests --check