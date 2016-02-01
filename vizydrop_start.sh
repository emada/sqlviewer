#!/usr/bin/env bash

export SQLPAD_PATH="`pwd`/sqlpad/db/"

cd vizydrop
python -m vizydrop.tpa $1.app &
cd -
