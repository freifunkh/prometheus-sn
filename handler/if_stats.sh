#!/bin/sh

interface=$1
result=$(ip -s link show $interface)

# helper function
line() { head -n "$1" | tail -n 1; }
trim_whitespace() { sed 's/[\ ]\+/ /g'; }

bytes_rx=$(echo "$result" | line 4 | trim_whitespace | cut -d " " -f 2)
bytes_tx=$(echo "$result" | line 6 | trim_whitespace | cut -d " " -f 2)
packets_rx=$(echo "$result" | line 4 | trim_whitespace | cut -d " " -f 3)
packets_tx=$(echo "$result" | line 6 | trim_whitespace | cut -d " " -f 3)

echo "{ \"name\": \"if_bytes_rx\", \"value\": $bytes_rx, \"interface\": \"$interface\" }"
echo "{ \"name\": \"if_bytes_tx\", \"value\": $bytes_tx, \"interface\": \"$interface\" }"
echo "{ \"name\": \"if_packets_rx\", \"value\": $packets_rx, \"interface\": \"$interface\" }"
echo "{ \"name\": \"if_packets_tx\", \"value\": $packets_tx, \"interface\": \"$interface\" }"
