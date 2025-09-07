import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import get_recent_alerts, add_alert

print("Testing Alert System...")

# Test adding alerts
alerts = [
    "⚠️ Blackspot ahead in 500 meters. Slow down.",
    "⚠️ Bumps ahead in 200 meters. Slow down.",
    "⚠️ School zone in 300 meters. Watch for children.",
    "⚠️ Sharp bend ahead in 400 meters. Reduce speed.",
    "⚠️ Traffic congestion in 600 meters. Prepare to stop."
]

for msg in alerts:
    add_alert(1, msg)
    print(f"VOICE ALERT: {msg.replace('⚠️', 'WARNING')}")  # Avoid encoding issue

# Test retrieving alerts
recent = get_recent_alerts(10)
print(f"\nRecent alerts: {len(recent)}")
for a in recent:
    print(f"- {a['timestamp']}: {a['message'].replace('⚠️', 'WARNING')}")

print("\nAlert system test completed successfully!")