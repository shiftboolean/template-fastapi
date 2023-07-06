#!/bin/sh -e
set -x

ruff app tests scripts --fix
black app tests scripts