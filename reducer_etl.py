#!/usr/bin/env python3
import sys

current_id = None
items = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        trans_id, item = line.split('\t', 1)
    except ValueError:
        sys.stderr.write("Bad line: {}\n".format(line))
        continue

    if current_id == trans_id:
        items.append(item)
    else:
        if current_id and items:
            items.sort()
            print(",".join(items))

        current_id = trans_id
        items = [item]

# Last transaction
if current_id and items:
    items.sort()
    print(",".join(items))