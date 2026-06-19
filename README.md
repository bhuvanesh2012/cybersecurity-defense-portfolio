# Internship Cybersecurity Portfolio

This repository contains two independent security engineering solutions built for my practical internship evaluation track. 

## 📂 Repository Architecture
- **`intrusion_detection_system/`**: An AI-driven anomaly and attack vector classifier using machine learning.
- **`personal_firewall/`**: A low-level host-based network packet capturing and filtering engine.

---

## 🤖 Project 1: Intrusion Detection System (IDS) with Machine Learning

### 🔹 Objective
To build a predictive traffic monitoring pipeline that uses Supervised Machine Learning to classify network connections as either standard system operations or malicious anomalies (such as rapid DoS connection floods or scanning signatures).

### 🔹 Technical Stack & Core Libraries
- **Language:** Python 3
- **Data Engineering:** Pandas, Numpy
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **Model Persistence:** Joblib

### 🔹 How it Works
1. **Feature Engineering:** Processes connection parameters including connection duration, total packet payload size, and network protocol types (TCP, UDP, ICMP).
2. **Ensemble Modeling:** Trains an ensemble **Random Forest Classifier** to build a statistical baseline of clean operations vs anomalous patterns.
3. **Model Serialization:** Saves the trained pipeline into an `ids_malicious_traffic_model.pkl` file for real-time deployment and inference scoring.

### 🔹 Verification & Execution
Run the model training pipeline:
```bash
python intrusion_detection_system/ids_model.py
```

## 🛡️ Project 2: Host-Based Personal Firewall Application
### 🔹 Objective
To engineer a functional host network packet manipulation engine capable of binding to local network interface adapters, performing stateless layer-3 (IP) and layer-4 (Port) rule verification, and dropping unauthorized packets.

### 🔹 Technical Stack & Core Libraries
- **Language:** Python 3
- **Network Driver Engine:** Scapy (Packet Capture Tool)
- **Dependencies:** Npcap (Windows network sniffer framework driver)

### 🔹 How it Works
1. **Raw Interface Hooking:** Intercepts real-time IP network traffic passing through your machine's physical network interface card (NIC).
2. **Access Control Matrices:**
Layer 3 Protection: Inspects source IPs against an active Threat Intelligence malicious blocklist array.
Layer 4 Protection: Automatically logs a [❌ DROP] flag against traffic hitting restricted or sensitive administrative ports (such as FTP Port 21, Telnet Port 23, or SMB Port 445).

### 🔹 Verification & Execution
- **⚠️ Note:** Requires raw socket access privileges. Open your terminal as an Administrator (Windows) or use sudo (Linux/macOS).

**PowerShell**
```bash
python personal_firewall/firewall.py
```

**Testing the rules actively:**
While the firewall is running in your Administrator window, open a separate terminal window and simulate a forbidden connection attempt using curl:

**Cmd**
```bash
curl.exe telnet://example.com:23
```

**Expected Output:** Your firewall console will instantly log a real-time dropping alert:
[❌ DROP] SECURITY ALERT: Blocked TCP Port 23 access attempt by [Your IP]!

### ⚙️ Global Dependencies Installation
To set up the environment required to run both applications locally, install the global manifest file:

```bash
pip install -r requirements.txt
