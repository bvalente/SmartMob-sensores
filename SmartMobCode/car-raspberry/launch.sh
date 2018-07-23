#!/bin/bash
MYADDR=$(grep address /etc/network/interfaces | awk -F ' ' '{print $2}')
#MYADDR=$(grep address interfaces | awk -F ' ' '{print $2}')
echo "Node IP address is: " $MYADDR
~

rm *.log
echo "removing log files "

python3 DevControlServer.py &
echo "DevControlServer is accepting connections at address: 127.0.0.1 "
sleep 5
python3 CommServer.py $MYADDR &
echo "CommServer is accepting connections at address: " $MYADDR
