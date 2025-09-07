from app.database import get_all_hazards, get_nearby_hazards, add_alert, get_recent_alerts

print("Testing database queries...")

# Test get all hazards
hazards = get_all_hazards()
print(f"Total hazards: {len(hazards)}")
for h in hazards:
    print(f"- {h['type']}: {h['description']} at ({h['lat']}, {h['lng']})")

# Test nearby hazards
nearby = get_nearby_hazards(-1.29, 36.82, 1000)
print(f"\nNearby hazards: {len(nearby)}")
for h in nearby:
    print(f"- {h['type']}: {h['description']}")

# Test add alert
add_alert(1, "⚠️ Blackspot ahead in 500 meters. Slow down.")
print("\nAlert added.")

# Test get recent alerts
alerts = get_recent_alerts()
print(f"Recent alerts: {len(alerts)}")
for a in alerts:
    print(f"- {a['timestamp']}: {a['message']}")

print("\nAll database tests passed!")