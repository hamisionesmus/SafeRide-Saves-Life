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

## 🧪 **Comprehensive Testing Instructions**

### **Prerequisites for Testing**
```bash
# System Requirements
- Python 3.8+
- pip package manager
- Web browser (Chrome, Firefox, Safari, Edge)
- Internet connection (for initial setup only)
- Audio output (speakers/headphones for voice alerts)
```

### **🚀 Quick Start Testing Setup**
```bash
# 1. Clone and setup
git clone https://github.com/hamisionesmus/SafeRide-Saves-Life.git
cd SafeRide-Saves-Life

# 2. Install dependencies
pip install -r requirements.txt

# 3. Initialize database with sample data
python app/database.py

# 4. Start the application
python app/main.py

# 5. Open browser and navigate to:
# Main App: http://localhost:8000
# Admin Panel: http://localhost:8000/admin
```

### **📋 Sample Data & Test Scenarios**

#### **Pre-loaded Test Hazards:**
The database comes pre-seeded with these test hazards:
- **Blackspot**: Accident-prone area (-1.2864, 36.8172)
- **Speed Bump**: Traffic calming device (-1.2921, 36.8219)
- **School Zone**: Child safety area (-1.2950, 36.8250)
- **Sharp Bend**: Road curve warning (-1.2980, 36.8280)
- **Traffic Congestion**: Heavy traffic zone (-1.3010, 36.8310)

#### **Test GPS Coordinates:**
Use these coordinates to trigger specific alerts:
- **Blackspot Alert**: Lat: -1.2864, Lng: 36.8172 (within 500m)
- **Speed Bump Alert**: Lat: -1.2921, Lng: 36.8219 (within 200m)
- **School Zone Alert**: Lat: -1.2950, Lng: 36.8250 (within 300m)

### **🧪 Automated Testing Suite**

#### **Database Tests**
```bash
python test_db.py
```
**Tests:** Database connections, CRUD operations, data integrity

#### **Alert System Tests**
```bash
python test_alerts.py
```
**Tests:** Alert generation, voice synthesis, multilingual support

#### **GPS Simulation Tests**
```bash
python test_gps_drive.py
```
**Tests:** Location tracking, hazard detection, proximity alerts

#### **LLM Integration Tests**
```bash
python test_llm.py
```
**Tests:** GPT-OSS model loading, multilingual generation

#### **Comprehensive Integration Test**
```bash
python final_test.py
```
**Tests:** End-to-end functionality, performance metrics

### **🖥️ Manual Testing Procedures**

#### **1. Core Functionality Testing**
```bash
# Start application
python app/main.py

# Test URLs:
# - Main Dashboard: http://localhost:8000/app
# - Admin Panel: http://localhost:8000/admin
# - API Status: http://localhost:8000/api/status
```

#### **2. Hazard Detection Testing**
- **Navigate to main dashboard**
- **Click "Test Alerts" button** to trigger all hazard types
- **Verify visual alerts appear** in the alert banner
- **Listen for voice alerts** (ensure speakers are on)
- **Check alert history** in the Recent Alerts section

#### **3. GPS Simulation Testing**
- **Click "Simulate Route" button**
- **Watch driver marker move** on the map
- **Observe proximity alerts** as marker approaches hazards
- **Verify real-time location updates**

#### **4. Multilingual Testing**
- **Test different languages** using API endpoints:
  ```
  /test_multilingual/en
  /test_multilingual/es
  /test_multilingual/fr
  /test_multilingual/de
  ```
- **Verify translated alerts** in different languages
- **Test voice synthesis** in multiple languages

#### **5. Admin Panel Testing**
- **Navigate to /admin**
- **Add new hazard** with custom coordinates
- **Edit existing hazard** and verify changes
- **Delete hazard** and confirm removal
- **Verify persistence** after page refresh

#### **6. Offline Functionality Testing**
- **Disable internet connection**
- **Refresh the application**
- **Verify all features work** without internet
- **Test service worker** caching
- **Confirm PWA installation** capability

#### **7. Mobile Responsiveness Testing**
- **Resize browser window** to mobile dimensions
- **Test touch interactions** on mobile devices
- **Verify map functionality** on small screens
- **Test admin panel** on mobile devices

### **🔧 API Testing Endpoints**

#### **Core API Endpoints:**
```bash
# System status
GET /api/status

# Get all hazards
GET /api/hazards

# Trigger test alerts
GET /test_alerts

# GPS simulation
GET /simulate_drive

# Multilingual testing
GET /test_multilingual/<language>

# Specific alert generation
GET /generate_alert/<hazard_type>/<language>
```

#### **Admin API Endpoints:**
```bash
# Add hazard
POST /admin/add

# Update hazard
POST /admin/update/<id>

# Delete hazard
POST /admin/delete/<id>
```

### **📊 Performance Testing**

#### **Response Time Testing:**
- **Hazard Detection**: Should respond in <100ms
- **Alert Generation**: Should complete in <2 seconds
- **Page Load**: Should load in <3 seconds
- **GPS Updates**: Should update every 3 seconds

#### **Load Testing:**
- **Multiple Alerts**: Test triggering 10+ simultaneous alerts
- **Database Operations**: Test CRUD operations under load
- **Memory Usage**: Monitor for memory leaks during extended use

### **🐛 Troubleshooting Common Issues**

#### **Application Won't Start:**
```bash
# Check Python version
python --version

# Verify dependencies
pip list | grep flask

# Check database file
ls -la saferide.db

# Clear cache and restart
rm -rf __pycache__/
python app/main.py
```

#### **Voice Alerts Not Working:**
```bash
# Install TTS dependencies
pip install pyttsx3 gtts

# Test voice synthesis
python -c "import pyttsx3; engine = pyttsx3.init(); engine.say('Test'); engine.runAndWait()"
```

#### **Map Not Loading:**
- Check internet connection for initial tile loading
- Verify Leaflet.js library is accessible
- Clear browser cache and reload

#### **Database Issues:**
```bash
# Reset database
rm saferide.db
python app/database.py
```

### **📈 Test Results & Validation**

#### **Expected Test Outcomes:**
- ✅ **All automated tests pass** without errors
- ✅ **Manual functionality works** as described
- ✅ **Performance metrics met** (response times, accuracy)
- ✅ **Offline functionality confirmed** (no internet required)
- ✅ **Multilingual support verified** (4+ languages)
- ✅ **Mobile responsiveness tested** on multiple devices

#### **Success Criteria:**
- **Hazard Detection Accuracy**: 100% for test scenarios
- **Voice Alert Success Rate**: 95%+ across all hazard types
- **GPS Simulation Precision**: ±5 meters accuracy
- **Response Time**: <100ms for hazard detection
- **Offline Functionality**: 100% features work without internet

### **🎯 Advanced Testing Scenarios**

#### **Edge Case Testing:**
- **Boundary Testing**: Hazards at exact distance limits
- **Concurrent Alerts**: Multiple hazards triggering simultaneously
- **Language Switching**: Rapid language changes during alerts
- **Memory Testing**: Extended operation without crashes

#### **Integration Testing:**
- **Cross-browser Testing**: Chrome, Firefox, Safari, Edge
- **Mobile Device Testing**: iOS Safari, Android Chrome
- **Network Interruption**: Test during connection drops
- **Battery Impact**: Monitor power consumption during use

### **📝 Test Documentation**

#### **Test Case Templates:**
```markdown
**Test Case ID:** TC_001
**Test Scenario:** Hazard Detection
**Preconditions:** Application running, GPS simulation active
**Test Steps:**
1. Navigate to main dashboard
2. Click "Test Alerts" button
3. Observe alert banner
4. Listen for voice alert
**Expected Result:** Visual and audio alerts trigger successfully
**Actual Result:** [Pass/Fail]
**Comments:** [Any observations]
```

#### **Bug Report Template:**
```markdown
**Bug ID:** BUG_001
**Title:** Voice alerts not working on Firefox
**Severity:** Medium
**Description:** Voice synthesis fails on Firefox browser
**Steps to Reproduce:**
1. Open app in Firefox
2. Trigger hazard alert
3. Voice alert does not play
**Expected Behavior:** Voice alert should play
**Actual Behavior:** No audio output
**Environment:** Firefox 115+, Windows 11
**Workaround:** Use Chrome or Edge
```

This comprehensive testing framework ensures SafeRide's reliability, performance, and functionality across all supported scenarios and environments.

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

**Project Lead**: Kilumo Hamisi
**Email**: kilumohamisi@gmail.com
**GitHub**: https://github.com/hamisionesmus/SafeRide-Saves-Life

---

## 🙏 **Special Thanks & Acknowledgements**

**We extend our heartfelt gratitude to GPT-OSS** for making this life-saving technology possible. Without the power of GPT-OSS models running completely offline, SafeRide's intelligent hazard detection, multilingual alerts, and safety assistance would not be possible. Thank you for enabling affordable, accessible AI that can help save lives worldwide.

**SafeRide - Because every life matters.** 
