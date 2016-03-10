#!/bin/sh

cd "$(dirname $0)/handler"

sh uptime.sh
sh if_stats.sh
ping -c 5 -i 0.2 8.8.8.8 | sh format_ping.sh "google-dns"
ping -c 5 -i 0.2 freifunk1.internetz.me | sh format_ping.sh "internetz.me"

# all fastd status sockets
for f in /var/run/fastd*.sock; do
    python3 fastd.py $f
done
