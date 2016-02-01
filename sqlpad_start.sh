#!/usr/bin/env bash

SQLPAD_PATH="`pwd`/sqlpad/db/"

sqlpad --dir $SQLPAD_PATH --port 3123 --save &
