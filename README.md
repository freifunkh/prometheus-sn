# prometheus gw scripts

These tools are developed for simple monitoring of some network
relevated information on the gateways.

# installation

1. Download

```
apt-get install curl
git clone <url>
```

2. fastd status socket

Add the following lines to your fastd.conf

```
status socket "/var/run/fastd.ffh-mesh-vpn.sock";

on up "
  chmod o+rw /var/run/fastd.ffh-mesh-vpn.sock
";
```

3. Setup

Setup the following cronjob to fill the data in the push-gateway. (Every minute)

```
* * * * * sh /path/to/gen.sh | curl -sgX POST --data-binary @- -H 'Lifetime: 2m' <URL>
```

(In hannover.freifunk.net the url for gw05 is ```http://\[fdca:ffee:8::108\]:9091/metrics/job/gw05```)
