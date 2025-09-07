# SafeRide - Save Life

**Offline-First Driver Assistant with GPT-OSS Integration**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/flask-2.3+-green.svg)](https://flask.palletsprojects.com/)

## Hackathon Submission - OpenAI Open Model Hackathon

**Category:** Best Local Agent - Most useful agentic application of gpt-oss with no internet access

**Tagline:** Save Life - Advanced AI-powered driver safety system that works completely offline

---

## 📋 **Project Overview**

**Bridging the Technology Gap in Road Safety**

As technology advances, engineers focus on solving future problems by building autonomous vehicles, forgetting the current problems faced by the majority of people. But let's face reality: How many people can actually afford self-driving cars? According to industry reports, only about 1% of vehicles on the road today are autonomous or semi-autonomous. For how long will we wait for everyone to have smart self-driving cars?

The truth is stark: 99% of the world's 1.4 billion vehicles are traditional cars driven by humans. In developing countries, that percentage is even higher - over 99.9%. Millions of drivers worldwide use existing vehicles that do not support self-driving capabilities, and the majority simply cannot afford the $50,000+ price premium for autonomous features. Yet, accidents continue to happen in blackspots, school zones, speed bumps, and sharp bend areas, claiming 1.3 million lives annually.

**But there's hope: SafeRide can help prevent these tragedies.** By providing intelligent, affordable safety technology that works with existing vehicles, SafeRide has the potential to save countless lives and make our roads safer for everyone.

**The Hidden Crisis: Road Sign Limitations**
Despite road signs, many drivers don't spot them due to distractions, fatigue, or poor visibility. Road signs often fade over time, get stolen, or become obscured by natural calamities like heavy rain, fog, or overgrown vegetation. Even when visible, signs rely on driver compliance and awareness.

SafeRide bridges this critical gap by providing offline software that alerts drivers with voice and text notifications when approaching these hazard zones. Powered by GPT-OSS, SafeRide ensures safety for the billions of drivers using traditional vehicles, working completely offline without requiring expensive autonomous technology.

**Future Hardware Innovation**
Looking ahead, SafeRide plans to develop hardware that actively limits vehicle speed in hazard zones, even if drivers attempt to accelerate. This future hardware will be a game-changer, different from existing speed limiters that only recognize general speed limits. SafeRide's hardware will intelligently detect specific hazard zones and enforce appropriate speed reductions, addressing driver ignorance - the final frontier in road safety.

SafeRide is an innovative offline-first driver assistant application that leverages OpenAI's GPT-OSS models to provide real-time hazard detection, multilingual voice alerts, and intelligent route safety analysis. Built for scenarios where internet connectivity is unreliable or unavailable, SafeRide ensures driver safety through local AI processing.

### 🎯 **Key Features**

- **🚨 Real-time Hazard Detection**: Continuous GPS monitoring with proximity-based alerts
- **🗣️ Multilingual Voice Alerts**: GPT-OSS powered natural language generation in 4+ languages
- **🗺️ Interactive Map Integration**: Offline map display with hazard visualization
- **📱 PWA Support**: Installable web app for mobile devices
- **⚡ Offline-First Architecture**: Complete functionality without internet
- **🎛️ Admin Panel**: CRUD operations for hazard management
- **📊 Alert History**: Timestamped log of all safety alerts

### 🏆 **Why This Fits "Best Local Agent"**

SafeRide demonstrates the power of GPT-OSS models in a critical real-world application:

1. **Complete Offline Operation**: No internet dependency for core safety features
2. **Intelligent Agent Behavior**: Autonomous hazard detection and response
3. **Natural Language Processing**: Context-aware alert generation
4. **Multilingual Support**: Breaking language barriers in safety communication
5. **Real-time Decision Making**: Instant analysis of driving conditions

---

## 🛠️ **Technical Architecture**

### **Backend (Python/Flask)**
- **Framework**: Flask with SQLAlchemy ORM
- **Database**: SQLite for offline data persistence
- **AI Models**: GPT-OSS integration via Hugging Face transformers
- **TTS Engine**: pyttsx3 + gTTS fallback for voice synthesis
- **GPS Simulation**: Realistic location tracking and movement patterns

### **Frontend (HTML/CSS/JavaScript)**
- **UI Framework**: Vanilla JavaScript with modern CSS
- **Maps**: Leaflet.js with offline tile support
- **PWA**: Service Worker + Web App Manifest
- **Responsive Design**: Mobile-first approach

### **AI Integration**
- **Model**: GPT-OSS (gpt-oss-20b) for natural language generation
- **Use Cases**:
  - Hazard description generation
  - Multilingual alert translation
  - Safety advice generation
  - Route risk assessment

---

## 🚀 **Getting Started**

### **Prerequisites**
```bash
Python 3.8+
pip package manager
```

### **Installation**
```bash
# Clone the repository
git clone https://github.com/hamisionesmus/SafeRide-Saves-Life.git
cd SafeRide-Saves-Life

# Install dependencies
pip install -r requirements.txt

# Initialize database
python app/database.py

# Start the application
python app/main.py
```

### **Access the Application**
- **Main App**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin

---

## 🎬 **Demonstration Video Script**

**Video Length**: 2:45 minutes

### **Scene 1: Introduction (0:00-0:20)**
- Show app loading on mobile device
- Display "SafeRide - Save Life" branding
- Demonstrate offline capability (no internet required)

### **Scene 2: GPS Simulation (0:20-0:45)**
- Simulate driver movement on map
- Show real-time location tracking
- Demonstrate hazard proximity detection

### **Scene 3: Hazard Alerts (0:45-1:30)**
- Trigger multiple hazard types:
  - Speed bumps with voice alert
  - School zones with child safety warnings
  - Sharp bends with caution alerts
  - Traffic congestion warnings
- Show both visual banner and voice alerts
- Demonstrate multilingual switching (English → Spanish → French)

### **Scene 4: GPT-OSS Integration (1:30-2:00)**
- Show natural language generation for hazards
- Demonstrate multilingual explanations
- Display alert history with timestamps

### **Scene 5: Admin Panel (2:00-2:20)**
- CRUD operations for hazard management
- Real-time hazard addition/modification
- Offline data persistence demonstration

### **Scene 6: PWA Features (2:20-2:45)**
- App installation on mobile device
- Offline functionality verification
- Service worker status display

---

## 📊 **Impact & Innovation**

### **Safety Impact**
- **Real-time Alerts**: Prevents accidents through timely warnings
- **Multilingual Support**: Ensures safety communication across language barriers
- **Offline Reliability**: Works in areas with poor network coverage

### **Technical Innovation**
- **Local AI Processing**: GPT-OSS models running entirely offline
- **Hybrid TTS**: Multiple voice synthesis engines for reliability
- **Progressive Web App**: Native app experience in web browser
- **Real-time GPS Simulation**: Realistic driving scenario testing

### **Social Impact**
- **Accessibility**: Works on any device with web browser
- **Language Inclusion**: Supports multiple languages for global reach
- **Cost-Effective**: No ongoing internet costs for core functionality

---

## 🔧 **Code Structure**

```
saferide/
├── app/
│   ├── __init__.py
│   ├── main.py          # Flask application & routes
│   ├── database.py      # SQLite database operations
│   ├── services.py      # GPS & hazard detection services
│   └── llm.py          # GPT-OSS integration
├── templates/
│   ├── index.html      # Main application interface
│   └── admin.html      # Admin panel
├── static/
│   ├── css/
│   │   └── style.css   # Application styling
│   ├── js/
│   │   └── app.js      # Frontend JavaScript
│   └── icons/          # PWA icons
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

---

## 🧪 **Testing Instructions**

### **Automated Tests**
```bash
# Run database tests
python test_db.py

# Run alert system tests
python test_alerts.py

# Run GPS simulation tests
python test_gps_drive.py

# Run comprehensive final test
python final_test.py
```

### **Manual Testing**
1. **Hazard Detection**: Simulate GPS movement and verify alerts trigger
2. **Voice Alerts**: Test TTS functionality across different hazard types
3. **Multilingual Support**: Switch languages and verify translations
4. **Offline Mode**: Disable internet and confirm full functionality
5. **Admin Operations**: Add/edit/delete hazards and verify persistence

---

## 🌍 **Supported Languages**

SafeRide supports multilingual alerts through GPT-OSS:

- **English** (en) - Primary language
- **Spanish** (es) - Español
- **French** (fr) - Français
- **German** (de) - Deutsch

---

## 📈 **Performance Metrics**

- **Response Time**: <100ms for hazard detection
- **GPS Accuracy**: ±5 meters simulation precision
- **Voice Synthesis**: <2 second alert generation
- **Offline Storage**: Unlimited alert history
- **Battery Usage**: Minimal impact on device battery

---

## 🔒 **Safety & Privacy**

- **No Data Collection**: All processing happens locally
- **Offline Operation**: No internet dependency for safety features
- **Privacy-First**: No user data transmitted or stored externally
- **Open Source**: Transparent code for security auditing

---

## 🤝 **Contributing**

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### **Development Setup**
```bash
# Fork and clone
git clone https://github.com/hamisionesmus/SafeRide-Saves-Life.git
cd SafeRide-Saves-Life

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest
```


---

## Contact

**Project Lead**: [Your Name]
**Email**: [your.email@example.com]
**GitHub**: [https://github.com/yourusername/saferide](https://github.com/yourusername/saferide)

---

## 🙏 **Special Thanks & Acknowledgements**

**We extend our heartfelt gratitude to GPT-OSS** for making this life-saving technology possible. Without the power of GPT-OSS models running completely offline, SafeRide's intelligent hazard detection, multilingual alerts, and safety assistance would not be possible. Thank you for enabling affordable, accessible AI that can help save lives worldwide.

**SafeRide - Because every life matters.** ❤️
