# Lesson 08 Lab Files

These files reproduce the harmless HTTP baseline and the controlled BitTorrent handshake used by Lesson 08.

## Included

- `baseline.html` - harmless negative control for HTTP availability.
- `bittorrent-responder.py` - one-shot responder that accepts one connection on Alpine TCP/80 and returns a deterministic 68-byte BitTorrent handshake.

## Deploy the baseline

```sh
mkdir -p /var/www/lesson08
cp baseline.html /var/www/lesson08/

nohup python3 -m http.server 80 \
  --bind 10.60.60.100 \
  --directory /var/www/lesson08 \
  >/tmp/lesson08-http.log 2>&1 &
```

Verify from Kali:

```bash
curl -I http://10.60.60.100/baseline.html
```

## Generate EICAR only inside the isolated lab

The raw EICAR string is deliberately not committed. Generate the exact 68-byte control on Alpine only when needed:

```sh
EICAR_PART1='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-'
EICAR_PART2='ANTIVIRUS-TEST-FILE!$H+H*'
printf '%s%s' "$EICAR_PART1" "$EICAR_PART2" \
  > /var/www/lesson08/eicar.com.txt
unset EICAR_PART1 EICAR_PART2

wc -c /var/www/lesson08/eicar.com.txt
sha256sum /var/www/lesson08/eicar.com.txt
```

Expected size and SHA-256:

```text
68 bytes
275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
```

Remove the generated file after the isolated test if it is no longer required.

## Run the controlled BitTorrent test

Stop the normal HTTP listener and start the one-shot responder on Alpine:

```sh
pkill -f 'python3 -m http.server 80' 2>/dev/null
python3 bittorrent-responder.py
```

It should display:

```text
Waiting for controlled BitTorrent handshake on 10.60.60.100:80...
```

Send the compact client handshake from Kali:

```bash
perl -e 'print "\x13BitTorrent protocol","\0"x48' \
  | nc -w2 10.60.60.100 80
```

Expected Alpine result:

```text
Received 68 bytes from ('10.10.10.100', <source-port>)
```

The responder exits after one connection. Restart it before every Application Control test so unrelated browser traffic cannot consume the listener.

## Restore the HTTP service

```sh
nohup python3 -m http.server 80 \
  --bind 10.60.60.100 \
  --directory /var/www/lesson08 \
  >/tmp/lesson08-http.log 2>&1 &
```
