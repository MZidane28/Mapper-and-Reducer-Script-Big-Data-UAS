import sys
import csv
import io

for line in sys.stdin:
    line = line.strip()
    reader = csv.reader(io.StringIO(line))
    parts = next(reader)
    
    if len(parts) < 2 or parts[0] == 'Transaction':
        continue
        
    transaction_id = parts[0]
    item_name = parts[1]

    print(f"{transaction_id}\t{item_name}")