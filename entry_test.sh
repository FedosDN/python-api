#!/bin/sh
sleep 5
while :
do
	sleep 10
    #python -m unittest test
    
    
    #python -m unittest test > tmp/test_result 2>tmp/test_errors
    # if [ $? = 0 ]; then
    #     echo 'Ok'
    # else
    #     cat ./tmp/test_errors
    # fi
done
exec "$@"