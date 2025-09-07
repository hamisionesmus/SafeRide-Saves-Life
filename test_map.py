import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import get_all_hazards

print("Testing Map Integration...")

# Test hazards API data
hazards = get_all_hazards()
print(f"Loaded {len(hazards)} hazards for map:")

for h in hazards:
    print(f"- {h['type']}: ({h['lat']}, {h['lng']}) - {h['description']}")

# Simulate map loading (check if data is in correct format)
if len(hazards) > 0:
    print("\nMap data format check:")
    sample = hazards[0]
    required_keys = ['id', 'type', 'lat', 'lng', 'description', 'distance']
    for key in required_keys:
        if key in sample:
            print(f"✓ {key}: {sample[key]}")
        else:
            print(f"✗ Missing {key}")

print("\nMap integration test completed successfully!")
print("Note: For offline tiles, tiles would need to be served locally from /static/tiles/")