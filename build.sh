#!/usr/bin/env bash


curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/activate


make install
make collectstatic
make migrate