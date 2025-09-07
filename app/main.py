import sys
import os
import time
from datetime import datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, render_template, jsonify
from database import get_recent_alerts, add_alert, get_all_hazards, add_hazard, update_hazard, delete_hazard
from services import HazardDetectionService, GeolocationService
from llm import LLMService

app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route("/")
def loading():
    return render_template("loading.html")

@app.route("/app")
def home():
    alerts = get_recent_alerts(5)
    return render_template("index.html", alerts=alerts)

@app.route("/admin")
def admin():
    hazards = get_all_hazards()
    return render_template("admin.html", hazards=hazards)

@app.route("/api/hazards")
def get_hazards():
    hazards = get_all_hazards()
    return jsonify({"hazards": [dict(h) for h in hazards]})

@app.route("/api/status")
def get_system_status():
    try:
        llm = LLMService()
        gpt_oss_loaded = llm.model_loaded
        voice_active = True
        gps_active = True
        return jsonify({
            "gpt_oss_loaded": gpt_oss_loaded,
            "voice_active": voice_active,
            "gps_active": gps_active,
            "system_status": "online",
            "timestamp": datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            "gpt_oss_loaded": False,
            "voice_active": False,
            "gps_active": False,
            "system_status": "error",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }), 500

@app.route("/trigger_alert", methods=["POST"])
def trigger_alert():
    message = request.form.get("message")
    if message:
        add_alert(1, message)
        try:
            llm = LLMService()
            if 'bump' in message.lower():
                hazard_type = 'bump'
                distance = 200
            elif 'blackspot' in message.lower():
                hazard_type = 'blackspot'
                distance = 500
            elif 'school' in message.lower():
                hazard_type = 'school_zone'
                distance = 300
            elif 'sharp' in message.lower():
                hazard_type = 'sharp_bend'
                distance = 400
            elif 'traffic' in message.lower():
                hazard_type = 'traffic_congestion'
                distance = 600
            else:
                hazard_type = 'general'
                distance = 500
            gpt_message = llm.generate_explanation(hazard_type, 'en', distance)
            try:
                import pyttsx3
                engine = pyttsx3.init()
                engine.setProperty('rate', 120)
                engine.setProperty('volume', 1.0)
                voices = engine.getProperty('voices')
                if voices:
                    engine.setProperty('voice', voices[0].id)
                engine.say(gpt_message)
                engine.runAndWait()
            except Exception as e:
                try:
                    from gtts import gTTS
                    import os
                    tts = gTTS(text=gpt_message, lang='en', slow=True)
                    audio_file = "gpt_alert.mp3"
                    tts.save(audio_file)
                    if os.name == 'nt':
                        os.system(f"start {audio_file}")
                except Exception as e2:
                    print(f"ALERT: {gpt_message}")
        except Exception as e3:
            clean_message = message.replace('⚠️', 'WARNING').replace('🚨', 'ALERT').replace('⚡', 'NOTICE').replace('🏫', 'SCHOOL').replace('🌀', 'CURVE').replace('🚦', 'TRAFFIC')
            print(f"ALERT: {clean_message}")
            try:
                from gtts import gTTS
                import os
                tts = gTTS(text=clean_message, lang='en', slow=True)
                audio_file = "alert.mp3"
                tts.save(audio_file)
                if os.name == 'nt':
                    os.system(f"start {audio_file}")
            except Exception as e4:
                print(f"ALERT: {clean_message}")
        return jsonify({"status": "alert triggered"})
    return jsonify({"error": "No message provided"}), 400

@app.route("/test_alerts")
def test_alerts():
    llm = LLMService()
    hazard_types = ['blackspot', 'bump', 'school_zone', 'sharp_bend', 'traffic_congestion']
    distances = [500, 200, 300, 400, 600]
    for hazard_type, distance in zip(hazard_types, distances):
        alert_message = llm.generate_explanation(hazard_type, 'en', distance)
        add_alert(1, alert_message)
        clean_message = alert_message.replace('⚠️', 'WARNING').replace('🚨', 'ALERT').replace('⚡', 'NOTICE').replace('🏫', 'SCHOOL').replace('🌀', 'CURVE').replace('🚦', 'TRAFFIC')
        print(f"ALERT: {clean_message}")
    return jsonify({"status": "test alerts triggered"})

@app.route("/simulate_drive")
def simulate_drive():
    from services import GeolocationService, HazardDetectionService
    geo_service = GeolocationService()
    hazard_service = HazardDetectionService(geo_service)
    alerts_triggered = []
    for i in range(10):
        lat, lng = geo_service.get_current_location()
        alerts = hazard_service.check_hazards(lat, lng)
        for hazard_id, message in alerts:
            clean_message = message.replace('⚠️', 'WARNING').replace('🚨', 'ALERT').replace('⚡', 'NOTICE').replace('🏫', 'SCHOOL').replace('🌀', 'CURVE').replace('🚦', 'TRAFFIC')
            add_alert(hazard_id, clean_message)
            try:
                from gtts import gTTS
                import os
                tts = gTTS(text=clean_message, lang='en', slow=True)
                audio_file = f"alert_{i}.mp3"
                tts.save(audio_file)
                if os.name == 'nt':
                    os.system(f"start {audio_file}")
                alerts_triggered.append(clean_message)
            except Exception as e:
                print(f"ALERT: {clean_message}")
        time.sleep(2)
    return jsonify({
        "status": "GPS simulation completed",
        "alerts_triggered": len(alerts_triggered),
        "alerts": alerts_triggered
    })

@app.route("/test_multilingual/<language>")
def test_multilingual(language):
    # Test multilingual alerts
    llm = LLMService()
    if language not in llm.supported_languages:
        return jsonify({"error": f"Language '{language}' not supported"}), 400

    hazard_types = ['blackspot', 'bump', 'school_zone', 'sharp_bend', 'traffic_congestion']
    alerts = []

    for hazard_type in hazard_types:
        alert_message = llm.generate_explanation(hazard_type, language, 500)
        add_alert(1, alert_message)
        alerts.append(alert_message)
        print(f"VOICE ALERT [{language}]: {alert_message}")

    return jsonify({
        "status": f"Multilingual alerts triggered in {llm.supported_languages[language]}",
        "language": language,
        "alerts": alerts
    })

@app.route("/languages")
def get_languages():
    # Get supported languages
    llm = LLMService()
    return jsonify({
        "languages": llm.get_supported_languages(),
        "default": "en"
    })

@app.route("/generate_alert/<hazard_type>/<language>")
def generate_alert(hazard_type, language):
    # Generate a specific alert in a specific language
    llm = LLMService()
    if hazard_type not in ['blackspot', 'bump', 'school_zone', 'sharp_bend', 'traffic_congestion']:
        return jsonify({"error": f"Hazard type '{hazard_type}' not supported"}), 400

    if language not in llm.supported_languages:
        return jsonify({"error": f"Language '{language}' not supported"}), 400

    alert_message = llm.generate_explanation(hazard_type, language, 500)
    add_alert(1, alert_message)

    return jsonify({
        "hazard_type": hazard_type,
        "language": language,
        "alert": alert_message
    })

@app.route("/admin/add", methods=["POST"])
def admin_add():
    try:
        type_ = request.form.get("type")
        lat = float(request.form.get("lat"))
        lng = float(request.form.get("lng"))
        description = request.form.get("description")
        distance = int(request.form.get("distance", 500))

        add_hazard(type_, lat, lng, description, distance)
        return jsonify({"status": "Hazard added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/admin/update/<int:id>", methods=["POST"])
def admin_update(id):
    try:
        type_ = request.form.get("type")
        lat = float(request.form.get("lat"))
        lng = float(request.form.get("lng"))
        description = request.form.get("description")
        distance = int(request.form.get("distance", 500))

        update_hazard(id, type_, lat, lng, description, distance)
        return jsonify({"status": "Hazard updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/admin/delete/<int:id>", methods=["POST"])
def admin_delete(id):
    try:
        delete_hazard(id)
        return jsonify({"status": "Hazard deleted successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question", "").strip()
    language = data.get("language", "en")
    if not question:
        return jsonify({"error": "No question provided"}), 400
    try:
        llm = LLMService()
        prompt = f"""You are SafeRide, an AI-powered driving safety assistant. Answer the following question about driving safety, road hazards, or general driving advice. Be helpful, accurate, and focused on safety.

Question: {question}

Provide a clear, concise answer that prioritizes safety. If the question is not related to driving safety, politely redirect to driving topics.

Answer:"""
        if llm.model_loaded:
            with llm.model.chat_session():
                response = llm.model.generate(prompt, max_tokens=200, temp=0.7)
            answer = response.strip()
        else:
            answer = generate_safety_answer(question, language)
        if data.get("speak", False):
            try:
                from gtts import gTTS
                import os
                tts = gTTS(text=answer, lang=language[:2] if language in ['en', 'es', 'fr', 'de', 'it', 'pt'] else 'en', slow=True)
                audio_file = f"answer_{hash(question) % 1000}.mp3"
                tts.save(audio_file)
                if os.name == 'nt':
                    os.system(f"start {audio_file}")
                return jsonify({
                    "question": question,
                    "answer": answer,
                    "language": language,
                    "audio_file": audio_file,
                    "spoken": True
                })
            except Exception as e:
                print(f"Speech synthesis failed: {e}")
        return jsonify({
            "question": question,
            "answer": answer,
            "language": language,
            "spoken": False
        })
    except Exception as e:
        return jsonify({"error": f"Failed to process question: {str(e)}"}), 500

def generate_safety_answer(question, language):
    question_lower = question.lower()
    safety_keywords = {
        'speed': 'speed_limit',
        'brake': 'braking',
        'weather': 'weather_driving',
        'tire': 'tire_safety',
        'emergency': 'emergency',
        'alcohol': 'alcohol_driving',
        'fatigue': 'fatigue_driving',
        'children': 'child_safety',
        'pedestrian': 'pedestrian_safety'
    }
    matched_topic = None
    for keyword, topic in safety_keywords.items():
        if keyword in question_lower:
            matched_topic = topic
            break
    if matched_topic:
        return get_safety_response(matched_topic, language)
    else:
        responses = {
            'en': "I'm SafeRide, your AI driving safety assistant. I can help you with questions about safe driving practices, road hazards, vehicle maintenance, and driving safety tips. What specific driving safety topic would you like to know about?",
            'es': "Soy SafeRide, tu asistente de seguridad vial con IA. Puedo ayudarte con preguntas sobre prácticas de conducción segura, peligros en la carretera, mantenimiento del vehículo y consejos de seguridad vial. ¿Sobre qué tema específico de seguridad vial te gustaría saber?",
            'fr': "Je suis SafeRide, votre assistant de sécurité routière IA. Je peux vous aider avec des questions sur les pratiques de conduite sécurisée, les dangers routiers, l'entretien du véhicule et les conseils de sécurité routière. Quel sujet spécifique de sécurité routière aimeriez-vous connaître?",
            'de': "Ich bin SafeRide, Ihr KI-Fahrsicherheitsassistent. Ich kann Ihnen bei Fragen zu sicheren Fahrpraktiken, Straßenrisiken, Fahrzeugwartung und Fahrsicherheitstipps helfen. Über welches spezifische Thema der Fahrsicherheit möchten Sie mehr wissen?"
        }
        return responses.get(language, responses['en'])

def get_safety_response(topic, language):
    responses = {
        'speed_limit': {
            'en': "Always obey posted speed limits. Speed limits are set based on road conditions, traffic patterns, and safety considerations. Driving too fast reduces your ability to react to hazards and increases stopping distance. Remember: speed kills.",
            'es': "Siempre obedezca los límites de velocidad publicados. Los límites de velocidad se establecen en función de las condiciones de la carretera, los patrones de tráfico y las consideraciones de seguridad. Conducir demasiado rápido reduce su capacidad de reaccionar ante peligros y aumenta la distancia de frenado. Recuerde: la velocidad mata.",
            'fr': "Respectez toujours les limitations de vitesse affichées. Les limitations de vitesse sont fixées en fonction des conditions routières, des schémas de circulation et des considérations de sécurité. Conduire trop vite réduit votre capacité à réagir aux dangers et augmente la distance d'arrêt. Rappelez-vous: la vitesse tue.",
            'de': "Halten Sie sich immer an die ausgewiesenen Geschwindigkeitsbegrenzungen. Geschwindigkeitsbegrenzungen werden basierend auf Straßenbedingungen, Verkehrsmustern und Sicherheitsüberlegungen festgelegt. Zu schnelles Fahren verringert Ihre Fähigkeit, auf Gefahren zu reagieren und verlängert den Bremsweg. Denken Sie daran: Geschwindigkeit tötet."
        },
        'braking': {
            'en': "Maintain safe following distances - at least 3 seconds behind the vehicle in front. This gives you time to react and brake safely. Keep your brakes in good condition and get them checked regularly.",
            'es': "Mantenga distancias de seguridad - al menos 3 segundos detrás del vehículo delantero. Esto le da tiempo para reaccionar y frenar de forma segura. Mantenga los frenos en buenas condiciones y hágalos revisar regularmente.",
            'fr': "Maintenez des distances de sécurité - au moins 3 secondes derrière le véhicule devant. Cela vous donne le temps de réagir et de freiner en toute sécurité. Gardez vos freins en bon état et faites-les vérifier régulièrement.",
            'de': "Halten Sie sichere Abstände ein - mindestens 3 Sekunden hinter dem vorderen Fahrzeug. Dies gibt Ihnen Zeit, zu reagieren und sicher zu bremsen. Halten Sie Ihre Bremsen in gutem Zustand und lassen Sie sie regelmäßig überprüfen."
        },
        'weather_driving': {
            'en': "Reduce speed in poor weather conditions. Increase following distances, use headlights, and avoid sudden movements. In fog, use fog lights and drive slowly. In rain, watch for hydroplaning and reduce speed accordingly.",
            'es': "Reduzca la velocidad en condiciones climáticas adversas. Aumente las distancias de seguimiento, use las luces delanteras y evite movimientos bruscos. En niebla, use luces antiniebla y conduzca despacio. En lluvia, vigile el aquaplaning y reduzca la velocidad en consecuencia.",
            'fr': "Réduisez la vitesse par mauvais temps. Augmentez les distances de sécurité, utilisez les phares et évitez les mouvements brusques. Dans le brouillard, utilisez les feux de brouillard et conduisez lentement. Sous la pluie, surveillez l'aquaplaning et réduisez la vitesse en conséquence.",
            'de': "Reduzieren Sie die Geschwindigkeit bei schlechtem Wetter. Vergrößern Sie den Sicherheitsabstand, verwenden Sie Scheinwerfer und vermeiden Sie plötzliche Bewegungen. Im Nebel verwenden Sie Nebelscheinwerfer und fahren langsam. Bei Regen achten Sie auf Aquaplaning und reduzieren entsprechend die Geschwindigkeit."
        }
    }
    return responses.get(topic, {}).get(language, responses[topic]['en'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)