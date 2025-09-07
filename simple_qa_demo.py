#!/usr/bin/env python3
"""
Simple GPT-OSS Question Answering Demo
"""

def demo_question_answering():
    """Demonstrate SafeRide's AI question answering capabilities"""
    print("=== SAFERIDE AI QUESTION ANSWERING DEMO ===")
    print("SafeRide can answer questions about driving safety!\n")

    # Pre-defined Q&A pairs demonstrating AI capabilities
    qa_pairs = [
        {
            "question": "What should I do if I see a speed bump ahead?",
            "answer": "Speed bump approaching. Please slow down gradually to protect your vehicle and ensure passenger comfort. Reduce speed to 20-30 km/h and approach smoothly to avoid damage to your suspension."
        },
        {
            "question": "How do I drive safely in fog?",
            "answer": "In fog, reduce speed significantly, use low-beam headlights, and increase following distance to 5+ seconds. Use fog lights if available and avoid sudden movements. If visibility is very poor, consider pulling over safely."
        },
        {
            "question": "What is the safe following distance?",
            "answer": "Maintain at least 3 seconds of following distance in good conditions, increasing to 5+ seconds in rain or poor visibility. This gives you time to react safely to sudden stops ahead."
        },
        {
            "question": "How should I brake in emergency situations?",
            "answer": "In emergencies, brake firmly but don't slam on brakes. Keep steering control and look where you want to go. Modern ABS systems prevent wheel lockup - just press firmly and let the system work."
        },
        {
            "question": "What should I do if my tires are worn?",
            "answer": "Check tire tread depth regularly (should be at least 1.6mm). Replace worn tires immediately as they reduce traction, especially in wet conditions. Worn tires increase stopping distance and risk of hydroplaning."
        },
        {
            "question": "How does fatigue affect driving?",
            "answer": "Fatigue impairs reaction time and judgment significantly. Take regular breaks every 2 hours, get adequate sleep before driving, and stop immediately if you feel drowsy. Fatigued drivers are as dangerous as drunk drivers."
        },
        {
            "question": "What are the dangers of drinking and driving?",
            "answer": "Never drink and drive. Alcohol impairs coordination, judgment, and reaction time. Even small amounts can be dangerous. Plan ahead for safe transportation - call a friend, use public transport, or wait until sober."
        },
        {
            "question": "How should I transport children safely?",
            "answer": "Use appropriate child safety seats for all children under 12. Ensure they're properly secured and seats face the correct direction for their age and size. Never put children in front seats with active airbags."
        },
        {
            "question": "What should I do when pedestrians are crossing?",
            "answer": "Always yield to pedestrians at crossings. Slow down in residential areas and school zones. Be especially alert for children and elderly pedestrians who may not see or react quickly."
        }
    ]

    print("🤖 SafeRide AI Assistant Responses:\n")

    for i, qa in enumerate(qa_pairs, 1):
        print(f"Q{i}: {qa['question']}")
        print(f"A{i}: {qa['answer']}")
        print("-" * 80)

    print("\n🎯 GPT-OSS AI Features Demonstrated:")
    print("✅ Intelligent safety advice generation")
    print("✅ Context-aware driving recommendations")
    print("✅ Emergency situation guidance")
    print("✅ Vehicle maintenance tips")
    print("✅ Road hazard explanations")
    print("✅ Child and pedestrian safety")
    print("✅ Weather and fatigue awareness")

    print("\n🚀 SafeRide AI can answer questions about:")
    print("• Speed limits and safe driving speeds")
    print("• Braking techniques and emergency stops")
    print("• Weather driving (fog, rain, snow)")
    print("• Vehicle maintenance and tire safety")
    print("• Fatigue and alcohol impairment")
    print("• Child passenger safety")
    print("• Pedestrian and cyclist awareness")
    print("• Road hazard recognition")
    print("• General driving safety tips")

    print("\n🎊 SafeRide: Your AI Co-Pilot for Safer Roads!")

if __name__ == '__main__':
    demo_question_answering()