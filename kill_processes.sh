#!/usr/bin/env bash

for file in `ls -R`
do
    echo -e "\n\n$file\n"
done

ps -aux | awk '{print $2"\t"$12}' > process.out

python get_particular_python_process_pids.py

for _ in `cat python_pids.out`
do
	kill -9 $_
	if [ $? == 0 ]; then
		echo "process $_ has been killed!"
	fi
done
