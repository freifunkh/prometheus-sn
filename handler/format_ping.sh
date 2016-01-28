#!/bin/sh

result=$(cat)
descr=$1

package_loss=$(echo "$result" | grep "packet loss" | cut -d" " -f 6 | tr -d "%")
roundtrip=$(echo "$result" | grep "rtt" | cut -d " " -f 4 | cut -d "/" -f 2)

echo "{ \"name\": \"ping_package_loss\", \"value\": $package_loss, \"descr\": \"$descr\" }"
echo "{ \"name\": \"ping_roundtrip\", \"value\": $roundtrip, \"descr\": \"$descr\" }"
