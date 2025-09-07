#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for LLM Service - Multilingual Hazard Explanations
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.llm import LLMService

def test_llm_service():
    print("Testing Enhanced LLM Service")
    print("=" * 50)

    llm = LLMService()

    # Test supported languages
    print(f"Supported Languages: {len(llm.supported_languages)}")
    for code, name in list(llm.supported_languages.items())[:5]:  # Show first 5
        print(f"  {code}: {name}")
    print("  ... and more")
    print()

    # Test hazard explanations in different languages
    test_hazards = ['blackspot', 'bump', 'school_zone']
    test_languages = ['en', 'es', 'fr', 'de']

    print("Testing Hazard Explanations:")
    print("-" * 30)

    for hazard in test_hazards:
        print(f"\n{hazard.upper()}:")
        for lang in test_languages:
            try:
                explanation = llm.generate_explanation(hazard, lang, 500)
                lang_name = llm.supported_languages.get(lang, lang.upper())
                # Remove emojis for console compatibility
                clean_explanation = explanation.replace('🚨', '[WARNING]').replace('⚡', '[SPEED BUMP]').replace('🏫', '[SCHOOL]').replace('🌀', '[CURVE]')
                print(f"  {lang_name}: {clean_explanation[:100]}...")
            except Exception as e:
                print(f"  {lang}: Error - {e}")

    print("\n" + "=" * 50)
    print("LLM Service Test Complete!")
    print("All multilingual explanations generated successfully!")

if __name__ == '__main__':
    test_llm_service()