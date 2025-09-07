#!/usr/bin/env python3
"""
Test GPT-OSS Question Answering System
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.llm import LLMService

def test_question_answering():
    """Test the GPT-OSS question answering system"""
    print("=== GPT-OSS QUESTION ANSWERING TEST ===")
    print("Testing SafeRide's AI assistant capabilities...\n")

    # Initialize the LLM service
    llm = LLMService()

    # Test questions
    test_questions = [
        "What should I do if I see a speed bump ahead?",
        "How do I drive safely in fog?",
        "What is the safe following distance?",
        "How should I brake in emergency situations?",
        "What should I do if my tires are worn?",
        "How does fatigue affect driving?",
        "What are the dangers of drinking and driving?",
        "How should I transport children safely?",
        "What should I do when pedestrians are crossing?",
        "Can you tell me about road safety in general?"
    ]

    print("🤖 SafeRide AI Assistant Responses:\n")

    for i, question in enumerate(test_questions, 1):
        print(f"Q{i}: {question}")

        try:
            # Create a driving safety focused prompt
            prompt = f"""You are SafeRide, an AI-powered driving safety assistant. Answer the following question about driving safety, road hazards, or general driving advice. Be helpful, accurate, and focused on safety.

Question: {question}

Provide a clear, concise answer that prioritizes safety. Keep it under 100 words.

Answer:"""

            if llm.model_loaded:
                # Use GPT-OSS model for intelligent response
                with llm.model.chat_session():
                    response = llm.model.generate(prompt, max_tokens=150, temp=0.7)
                answer = response.strip()
                print(f"🤖 GPT-OSS: {answer}")
            else:
                # Use template-based response
                answer = generate_template_answer(question)
                print(f"🤖 Template: {answer}")

        except Exception as e:
            # Fallback to template
            answer = generate_template_answer(question)
            print(f"🤖 Template: {answer}")
            print(f"   (GPT-OSS failed: {str(e)[:50]}...)")

        print("-" * 80)
        print()

def generate_template_answer(question):
    """Generate template-based answers for common questions"""
    question_lower = question.lower()

    if "speed bump" in question_lower:
        return "⚡ Speed bump approaching. Please slow down gradually to protect your vehicle and ensure passenger comfort. Reduce speed to 20-30 km/h and approach smoothly."

    elif "fog" in question_lower:
        return "🌫️ In fog, reduce speed significantly, use low-beam headlights, and increase following distance to 5+ seconds. Use fog lights if available and avoid sudden movements."

    elif "following distance" in question_lower:
        return "📏 Maintain at least 3 seconds of following distance in good conditions, increasing to 5+ seconds in rain or poor visibility. This gives you time to react safely."

    elif "brake" in question_lower or "emergency" in question_lower:
        return "🛑 In emergencies, brake firmly but don't slam on brakes. Keep steering control and look where you want to go. Modern ABS systems prevent wheel lockup."

    elif "tire" in question_lower:
        return "🛞 Check tire tread depth regularly (should be at least 1.6mm). Replace worn tires immediately as they reduce traction, especially in wet conditions."

    elif "fatigue" in question_lower:
        return "😴 Fatigue impairs reaction time and judgment. Take regular breaks every 2 hours, get adequate sleep before driving, and stop immediately if you feel drowsy."

    elif "alcohol" in question_lower or "drinking" in question_lower:
        return "🚫 Never drink and drive. Alcohol impairs coordination, judgment, and reaction time. Even small amounts can be dangerous. Plan ahead for safe transportation."

    elif "children" in question_lower:
        return "👶 Use appropriate child safety seats for all children under 12. Ensure they're properly secured and seats face the correct direction for their age and size."

    elif "pedestrian" in question_lower:
        return "🚶 Always yield to pedestrians at crossings. Slow down in residential areas and school zones. Be especially alert for children and elderly pedestrians."

    else:
        return "I'm SafeRide, your AI driving safety assistant. I can help with questions about speed limits, braking, weather driving, vehicle maintenance, emergency procedures, and general road safety. What specific driving safety topic interests you?"

if __name__ == '__main__':
    test_question_answering()