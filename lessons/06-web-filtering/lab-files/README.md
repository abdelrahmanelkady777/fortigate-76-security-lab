# Lesson 06 HTTP Controls

These harmless files reproduce the three deterministic HTTP targets used by Lesson 06:

| File | Intended Web Filter result |
| --- | --- |
| `allowed.html` | Unmatched negative control; allowed normally |
| `blocked.html` | Exact local URL-filter match; blocked |
| `monitored.html` | Exact local URL-filter match; allowed and logged |

Deploy them beneath the inherited Alpine document root:

```sh
mkdir -p /var/www/lesson04/lesson06
cp allowed.html blocked.html monitored.html /var/www/lesson04/lesson06/
```

The expected HTTP paths are:

```text
/lesson06/allowed.html
/lesson06/blocked.html
/lesson06/monitored.html
```

The exact lowercase directory name and the zero in `lesson06` matter when the FortiGate URL-filter type is `Simple`.

