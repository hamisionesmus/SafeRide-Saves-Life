# 🚀 SafeRide - Quick Start Guide for Judges

## ⚡ **5-Minute Setup & Demo**

### **Step 1: Clone & Install (2 minutes)**
```bash
git clone https://github.com/yourusername/saferide.git
cd saferide
pip install -r requirements.txt
```

### **Step 2: Initialize Database (30 seconds)**
```bash
python app/database.py
```

### **Step 3: Start Application (30 seconds)**
```bash
python app/main.py
```

### **Step 4: Access Application**
- **Main App:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

---

## 🎯 **Key Features to Test**

### **1. GPS Simulation & Hazard Detection**
- Click around the map to simulate GPS movement
- Watch for automatic hazard proximity alerts
- Verify offline operation (disconnect internet)

### **2. Voice Alerts & Multilingual Support**
- Trigger alerts using the test buttons
- Switch between languages (EN/ES/FR/DE)
- Listen to voice synthesis (pyttsx3/gTTS)

### **3. GPT-OSS Integration**
- Ask questions in the chat interface
- See natural language generation
- Test multilingual translations

### **4. Admin Panel**
- Add/edit/delete hazards
- Verify real-time map updates
- Test offline data persistence

---

## 🧪 **Test Commands**

### **Run All Tests**
```bash
python final_test.py
```

### **Individual Test Components**
```bash
python test_db.py          # Database operations
python test_alerts.py      # Alert system
python test_gps_drive.py   # GPS simulation
python test_llm.py         # GPT-OSS integration
```

---

## 🔧 **System Requirements**

- **Python:** 3.8+
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 40GB for GPT-OSS models
- **Browser:** Modern browser with PWA support

---

## 📊 **Expected Performance**

- **Startup Time:** <30 seconds
- **Response Time:** <100ms for alerts
- **GPS Simulation:** Real-time updates
- **Voice Synthesis:** <2 seconds per alert

---

## 🎬 **Demo Script**

1. **Show Offline Capability** - Disconnect internet, verify functionality
2. **Demonstrate GPS Tracking** - Simulate driving route
3. **Trigger Hazard Alerts** - Show visual + voice alerts
4. **Test Multilingual Support** - Switch languages
5. **GPT-OSS Showcase** - Natural language generation
6. **Admin Operations** - CRUD hazard management

---

## 🆘 **Troubleshooting**

### **Common Issues:**
- **Port 8000 occupied:** Change port in `app/main.py`
- **GPT-OSS model loading:** May take 2-3 minutes first time
- **Voice synthesis:** Requires speakers/audio output
- **Map tiles:** May need internet for initial load

### **Quick Fixes:**
```bash
# Clear database and restart
rm saferide.db
python app/database.py

# Force reload application
pkill -f "python app/main.py"
python app/main.py
```

---

## 📞 **Need Help?**

**Contact:** [your.email@example.com]  
**Repository:** https://github.com/yourusername/saferide  
**Documentation:** See `README.md` and `hackathon_submission.md`

---

**SafeRide - Ready for judging! 🚗❤️**