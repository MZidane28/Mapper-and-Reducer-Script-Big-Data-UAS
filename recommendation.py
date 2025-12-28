import os
import sys
import csv

class RecommendationEngine:
    def __init__(self, data_file):
        """
        Initializes the engine by loading the Hadoop CSV output into a dictionary.
        """
        self.rules = {}
        self._load_data(data_file)

    def _load_data(self, filepath):
        if not os.path.exists(filepath):
            # Fail silently or raise error depending on API needs
            print(f"Error: File '{filepath}' not found.")
            return

        with open(filepath, 'r', encoding='utf-8') as f:
            # Use the csv module to handle parsing robustly
            reader = csv.reader(f)
            
            # Skip the header row (Item1,Item2,Count)
            next(reader, None)

            for row in reader:
                # Row format: ['ItemA', 'ItemB', 'Count']
                if len(row) < 3:
                    continue
                
                try:
                    item_a = row[0].strip()
                    item_b = row[1].strip()
                    count = int(row[2].strip())

                    # Store bidirectional relationships
                    # (If A is bought with B, B is also bought with A)
                    self._add_rule(item_a, item_b, count)
                    self._add_rule(item_b, item_a, count)
                except ValueError:
                    continue

    def _add_rule(self, key, value, count):
        if key not in self.rules:
            self.rules[key] = []
        self.rules[key].append((value, count))

    def recommend(self, item_name):
        """
        Returns the single best recommendation or None if not found.
        """
        # Case-insensitive lookup
        lookup_key = None
        for key in self.rules:
            if key.lower() == item_name.lower():
                lookup_key = key
                break
        
        if not lookup_key:
            return None

        # Sort by count (descending) and pick top 1
        candidates = self.rules[lookup_key]
        candidates.sort(key=lambda x: x[1], reverse=True)
        
        # Return the best match item name
        return candidates[0][0]

if __name__ == "__main__":
    # check for command line argument
    if len(sys.argv) < 2:
        print("Usage: python recommendation.py <Item Name>")
        sys.exit(1)
        
    input_item = sys.argv[1]
    
    engine = RecommendationEngine('mapreduce_result.csv')
    
    result = engine.recommend(input_item)
    
    if result:
        print(result)
    else:
        print("No recommendation found")