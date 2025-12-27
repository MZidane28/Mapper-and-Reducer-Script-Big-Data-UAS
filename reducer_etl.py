import sys

current_id = None
items = []

for line in sys.stdin:
    line = line.strip()
    try:
        trans_id, item = line.split('\t', 1)
    except ValueError:
        continue

    # If we are on the same transaction ID, add item to list
    if current_id == trans_id:
        items.append(item)
    else:
        # New transaction detected! Emit the previous basket.
        if current_id and items:
            items.sort()
            print(",".join(items))
        
        # Reset for new transaction
        current_id = trans_id
        items = [item]

# Don't forget the last transaction
if current_id and items:
    items.sort()
    print(",".join(items))