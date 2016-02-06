#!/bin/sh

cd "$(dirname $0)/handler"

sh uptime.sh
sh if_stats.sh enp0s25
sh if_stats.sh wlp3s0
ping -c 5 -i 0.2 8.8.8.8 | sh format_ping.sh "google dns"
ping -c 5 -i 0.2 sponge.gatrobe.de | sh format_ping.sh "sponge"

python3 fastd.py /var/run/fastd.sock
