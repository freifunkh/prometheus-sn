#!/bin/sh

cd "$(dirname $0)/handler"

sh if_stats.sh freifunk
sh if_stats.sh bat0
sh ping.sh 8.8.8.8
sh ping.sh sponge.gatrobe.de

python3 fastd.py /var/run/fastd.sock
