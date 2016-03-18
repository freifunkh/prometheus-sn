#!/bin/sh

usock_path="$1"

stats=$(nc -U "$usock_path")

for line in $stats; do
	identifier=$(echo "$line" | cut -d ":" -f 1)
	bytes=$(echo "$line" | cut -d ":" -f 2)
	packets=$(echo "$line" | cut -d ":" -f 3)

	echo "bpfcountd_packets{$identifier} $packets"
	echo "bpfcountd_bytes{$identifier} $bytes"
done
