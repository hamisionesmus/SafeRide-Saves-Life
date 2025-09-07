#!/usr/bin/env python3
"""
Test SafeRide Voice Alerts
"""
print("SPEAKER: SafeRide Voice Alert Test Starting...")

try:
    from gtts import gTTS
    import os

    # Test messages
    test_messages = [
        "WARNING: Blackspot ahead in 500 meters. Slow down.",
        "NOTICE: Speed bump approaching. Please slow down gradually.",
        "SCHOOL: School zone in 300 meters. Children may be crossing.",
        "CURVE: Sharp bend in 400 meters. Reduce speed immediately.",
        "TRAFFIC: Heavy traffic congestion in 600 meters. Expect delays."
    ]

    print("GENERATING: Creating voice alerts...")

    for i, message in enumerate(test_messages, 1):
        print(f"\nALERT {i}: {message}")

        # Generate TTS
        tts = gTTS(text=message, lang='en', slow=True)
        audio_file = f"saferide_alert_{i}.mp3"
        tts.save(audio_file)

        print(f"SUCCESS: Audio file created: {audio_file}")

        # Try to play it
        try:
            if os.name == 'nt':  # Windows
                print("PLAYING: Starting audio playback...")
                os.system(f"start {audio_file}")
            else:
                print("READY: Audio file ready for playback")
        except Exception as play_error:
            print(f"WARNING: Playback failed: {play_error}")

    print("\nSUCCESS: All voice alerts generated successfully!")
    print("CHECK: Audio files created and playback attempted!")

except ImportError as e:
    print(f"ERROR: Import Error: {e}")
    print("HINT: Make sure gTTS is installed: pip install gtts")

except Exception as e:
    print(f"ERROR: Voice Test Failed: {e}")
    import traceback
    traceback.print_exc()

print("\nCOMPLETE: SafeRide Voice Test Complete!")