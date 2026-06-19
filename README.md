# Cybersecurity Internship Capstone Portfolio

This repository contains my two finalized security engineering project implementations completed for my practical evaluation track. 

## 📂 Repository Architecture
- **`intrusion_detection_system/`**: An AI-driven anomaly and attack vector classifier.
- **`personal_firewall/`**: A low-level host-based network packet capturing and filtering engine.

---

## 🤖 1. Intrusion Detection System (IDS) with Machine Learning

### Objective
To build an automated traffic monitoring script that leverages Supervised Machine Learning to classify connections as either normal system operations or malicious anomalies (such as rapid DoS connection floods or aggressive scanning signatures).

### Technical Stack
- **Language:** Python 3
- **Libraries:** Scikit-Learn, Pandas, Numpy, Joblib

### How it Works & Features
1. **Feature Engineering:** Parses and processes core connection parameters: connection duration, total packet size payload, and network layer protocol types (TCP, UDP, ICMP).
2. **Ensemble Classifier:** Trains a **Random Forest Classifier** to establish a tight statistical baseline of normal operations vs anomalous behavior.
3. **Model Serialization:** Saves the trained pipeline into a `.pkl` object file for instant production deployment and inference scoring.

### Running the IDS Code
```bash
python intrusion_detection_system/ids_model.py
```
### Running the Firewall Code
```bash
python personal_firewall/firewall.py
