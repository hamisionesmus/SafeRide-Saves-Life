#!/usr/bin/env python3
"""
Simple LLM Integration Demo - No Emojis for Windows Compatibility
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.llm import LLMService
from app.database import init_db, seed_data, add_alert, get_recent_alerts

def demo():
    print("SAFERIDE DRIVER ASSISTANT - LLM INTEGRATION DEMO")
    print("=" * 55)

    # Initialize services
    print("Initializing Database and LLM Service...")
    init_db()
    seed_data()
    llm = LLMService()
    print("Ready!")

    # Test multilingual alerts
    print("\nGENERATING MULTILINGUAL HAZARD ALERTS:")
    print("-" * 45)

    test_cases = [
        ('blackspot', 'en', 500),
        ('bump', 'es', 200),
        ('school_zone', 'fr', 300),
        ('sharp_bend', 'de', 400),
        ('traffic_congestion', 'ar', 600)
    ]

    for hazard_type, language, distance in test_cases:
        alert = llm.generate_explanation(hazard_type, language, distance)
        add_alert(1, alert)

        lang_name = llm.supported_languages.get(language, language.upper())
        # Remove emojis for console compatibility
        clean_alert = alert.replace('🚨', '[WARNING]').replace('⚡', '[BUMP]').replace('🏫', '[SCHOOL]').replace('🌀', '[CURVE]').replace('🚦', '[TRAFFIC]')
        print(f"{lang_name}: {clean_alert[:90]}...")

    # Show recent alerts
    print("\nRECENT ALERTS LOG:")
    print("-" * 20)
    alerts = get_recent_alerts(3)
    for i, alert in enumerate(alerts, 1):
        clean_msg = alert['message'].replace('🚨', '[W]').replace('⚡', '[B]').replace('🏫', '[S]').replace('🌀', '[C]').replace('🚦', '[T]')
        print(f"{i}. {clean_msg[:70]}...")

    print("\n" + "=" * 55)
    print("LLM INTEGRATION SUCCESSFUL!")
    print("Features:")
    print("- 10 Languages Supported")
    print("- Natural Explanations")
    print("- Distance Integration")
    print("- Database Logging")
    print("- Real-time Generation")
    print("=" * 55)

if __name__ == '__main__':
    demo()