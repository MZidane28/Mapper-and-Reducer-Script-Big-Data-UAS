#!/usr/bin/env python3
import sys
import csv
import io

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        reader = csv.reader(io.StringIO(line))
        parts = next(reader)

        # Skip header reliably (handle BOM)
        if len(parts) < 2 or parts[0].lstrip('\ufeff') == 'Transaction':
            continue

        transaction_id = parts[0]
        item_name = parts[1]

        # Use .format() for Python 3.5 compatibility
        print("{}\t{}".format(transaction_id, item_name))

    except Exception as e:
        sys.stderr.write("Error processing line: {} | {}\n".format(line, str(e)))
        continue