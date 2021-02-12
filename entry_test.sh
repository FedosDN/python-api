#!/bin/sh
sleep 5
python run.py
while :
do
	sleep 10
    python -m unittest test
done
exec "$@"