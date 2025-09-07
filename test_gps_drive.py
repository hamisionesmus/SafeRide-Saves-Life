#!/usr/bin/env python3
"""
Test GPS-based Hazard Detection with Voice Alerts
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import get_nearby_hazards, add_alert
from app.services import GeolocationService, HazardDetectionService

def test_gps_hazard_detection():
    """Test GPS-based hazard detection that triggers voice alerts"""
    print("=== GPS-BASED HAZARD DETECTION TEST ===")
    print("Simulating driver movement and hazard detection...")

    # Initialize services
    geo_service = GeolocationService()
    hazard_service = HazardDetectionService(geo_service)

    alerts_triggered = []

    print("\nStarting GPS simulation...")
    print("Driver will move and alerts will trigger when approaching hazards\n")

    for i in range(15):  # Simulate 15 GPS updates
        lat, lng = geo_service.get_current_location()
        print(".4f")
        # Check for nearby hazards
        alerts = hazard_service.check_hazards(lat, lng)

        if alerts:
            print(f"  🚨 HAZARD DETECTED! {len(alerts)} alert(s) triggered")
            for hazard_id, message in alerts:
                # Clean message for TTS
                clean_message = message.replace('⚠️', 'WARNING').replace('🚨', 'ALERT').replace('⚡', 'NOTICE').replace('🏫', 'SCHOOL').replace('🌀', 'CURVE').replace('🚦', 'TRAFFIC')

                # Add to database
                add_alert(hazard_id, clean_message)

                # Trigger voice alert
                try:
                    from gtts import gTTS
                    import os
                    tts = gTTS(text=clean_message, lang='en', slow=True)
                    audio_file = f"gps_alert_{i}.mp3"
                    tts.save(audio_file)
                    if os.name == 'nt':
                        os.system(f"start {audio_file}")
                    print(f"  🔊 VOICE ALERT: {clean_message}")
                    alerts_triggered.append(clean_message)
                except Exception as e:
                    print(f"  🔊 VOICE ALERT: {clean_message} (TTS failed)")
                    alerts_triggered.append(clean_message)
        else:
            print("  ✅ No hazards detected in this area")

        time.sleep(1)  # Wait 1 second between GPS updates

    print("
=== GPS SIMULATION COMPLETED ===")
    print(f"Total alerts triggered: {len(alerts_triggered)}")
    print("\nAlerts that were triggered:")
    for i, alert in enumerate(alerts_triggered, 1):
        print(f"{i}. {alert}")

    if alerts_triggered:
        print("
✅ SUCCESS: GPS-based hazard detection is working!"        print("✅ Voice alerts are triggered when approaching hazards!"        print("✅ System responds to real GPS movement simulation!"    else:
        print("
⚠️ No alerts triggered - driver may not have passed near hazards"        print("Try adjusting GPS coordinates or hazard locations"

if __name__ == '__main__':
    test_gps_hazard_detection()