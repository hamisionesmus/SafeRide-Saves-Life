import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import get_all_hazards, get_recent_alerts, add_alert
from app.services import GeolocationService, HazardDetectionService
from app.llm import LLMService

print("SafeRide Driver Assistant - Final Test")

hazards = get_all_hazards()
print(f"Database: {len(hazards)} hazards loaded")

geo_service = GeolocationService()
lat, lng = geo_service.get_current_location()
print(f"GPS: ({lat:.4f}, {lng:.4f})")

hazard_service = HazardDetectionService(geo_service)
alerts = hazard_service.check_hazards(lat, lng)
print(f"Hazard Detection: {len(alerts)} alerts triggered")

llm = LLMService()
for hazard_type in ['blackspot', 'bump']:
    explanation = llm.generate_explanation(hazard_type, 'en')
    print(f"LLM: {hazard_type} - {explanation[:50]}...")

print("All systems tested successfully")