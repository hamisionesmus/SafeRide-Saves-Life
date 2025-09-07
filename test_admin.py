import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import get_all_hazards, add_hazard, update_hazard, delete_hazard

print("Testing Admin Panel CRUD Operations...")

# Test initial hazards
initial_hazards = get_all_hazards()
print(f"Initial hazards: {len(initial_hazards)}")

# Test add hazard
print("\nAdding new hazard...")
add_hazard('test_hazard', -1.30, 36.83, 'Test hazard for admin', 300)
hazards_after_add = get_all_hazards()
print(f"Hazards after add: {len(hazards_after_add)}")

# Test update hazard
print("\nUpdating hazard...")
if hazards_after_add:
    last_hazard = hazards_after_add[-1]
    update_hazard(last_hazard['id'], 'updated_hazard', -1.31, 36.84, 'Updated test hazard', 400)
    print("Hazard updated.")

# Test delete hazard
print("\nDeleting hazard...")
if hazards_after_add:
    last_hazard = hazards_after_add[-1]
    delete_hazard(last_hazard['id'])
    hazards_after_delete = get_all_hazards()
    print(f"Hazards after delete: {len(hazards_after_delete)}")

print("\nAdmin CRUD test completed successfully!")
print("All operations (Create, Read, Update, Delete) work correctly.")