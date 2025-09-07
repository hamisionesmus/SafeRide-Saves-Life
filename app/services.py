import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
import random
from app.database import get_nearby_hazards, add_alert
from app.llm import LLMService

class GeolocationService:
    def __init__(self):
        self.current_lat = -1.29
        self.current_lng = 36.82
        self.speed = 0  # km/h

    def get_current_location(self):
        self.current_lat += random.uniform(-0.001, 0.001)
        self.current_lng += random.uniform(-0.001, 0.001)
        return self.current_lat, self.current_lng

    def simulate_gps(self):
        while True:
            lat, lng = self.get_current_location()
            yield lat, lng
            time.sleep(1)

class HazardDetectionService:
    def __init__(self, geolocation_service, language='en'):
        self.geolocation = geolocation_service
        self.alerted_hazards = set()  # To avoid repeated alerts
        self.llm = LLMService()
        self.language = language  # Default language

    def check_hazards(self, lat, lng, radius=1000):
        hazards = get_nearby_hazards(lat, lng, radius)
        alerts = []
        
        for hazard in hazards:
            hazard_id = hazard['id']
            if hazard_id not in self.alerted_hazards:
                message = self.generate_alert_message(hazard)
                alerts.append((hazard_id, message))
                self.alerted_hazards.add(hazard_id)
        
        return alerts

    def generate_alert_message(self, hazard):
        return self.llm.generate_explanation(
            hazard['type'],
            language=self.language,
            distance=hazard['distance']
        )

    def set_language(self, language):
        if language in self.llm.supported_languages:
            self.language = language
            return True
        return False

    def get_supported_languages(self):
        return self.llm.get_supported_languages()

    def trigger_alert(self, hazard_id, message):
        add_alert(hazard_id, message)
        print(f"ALERT: {message}")

    def run_detection(self):
        for lat, lng in self.geolocation.simulate_gps():
            alerts = self.check_hazards(lat, lng)
            for hazard_id, message in alerts:
                self.trigger_alert(hazard_id, message)
            if len(self.alerted_hazards) >= 5:
                break

if __name__ == '__main__':
    geo_service = GeolocationService()
    hazard_service = HazardDetectionService(geo_service)
    hazard_service.run_detection()