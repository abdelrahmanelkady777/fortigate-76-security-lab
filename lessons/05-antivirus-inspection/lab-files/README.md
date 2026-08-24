# Lesson 05 Lab Files

This directory documents the deterministic controls used by Lesson 05.

## Included

- `benign.txt` - harmless 33-byte negative control.

Expected SHA-256:

```text
faa50486471b5958a718d6bdb16e113a5dcc8d26c84f876ed43a3ea3ef88ca7a
```

## Generated only inside the isolated lab

The EICAR test string and its ZIP archive are deliberately not committed. Although EICAR is harmless, endpoint-security products intentionally detect and quarantine it.

Generate the exact 68-byte control on Alpine only when needed:

```sh
EICAR_PART1='X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-'
EICAR_PART2='ANTIVIRUS-TEST-FILE!$H+H*'
printf '%s%s' "$EICAR_PART1" "$EICAR_PART2" \
  > /var/www/lesson04/eicar.com.txt
unset EICAR_PART1 EICAR_PART2

wc -c /var/www/lesson04/eicar.com.txt
sha256sum /var/www/lesson04/eicar.com.txt
```

Expected SHA-256:

```text
275a021bbfb6489e54d471899f7db9d1663fc695ec2fe2a2c4538aabf651fd0f
```

Derived controls:

```sh
dd if=/dev/zero \
  of=/var/www/lesson04/large-benign.bin \
  bs=1M count=2

cd /var/www/lesson04
python3 -m zipfile -c benign.zip benign.txt
python3 -m zipfile -c eicar.zip eicar.com.txt
```

Delete the generated EICAR artifacts after the lesson if the isolated lab no longer needs them.
