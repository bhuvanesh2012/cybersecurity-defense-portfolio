import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def generate_mock_traffic_data(n_samples=1000):
    """Simulates realistic network traffic for Normal and Anomaly states."""
    np.random.seed(42)
    
    # Normal Traffic (Low frequency, standard packet sizes)
    normal_duration = np.random.uniform(0.1, 2.0, int(n_samples * 0.8))
    normal_packet_size = np.random.normal(500, 100, int(n_samples * 0.8))
    normal_protocol = np.random.choice([0, 1, 2], int(n_samples * 0.8)) # 0: TCP, 1: UDP, 2: ICMP
    normal_label = np.zeros(int(n_samples * 0.8))
    
    # Malicious Traffic (Rapid bursts, highly irregular packet sizes)
    malicious_duration = np.random.uniform(0.01, 0.05, int(n_samples * 0.2))
    malicious_packet_size = np.random.normal(1500, 50, int(n_samples * 0.2))
    malicious_protocol = np.random.choice([0, 2], int(n_samples * 0.2))
    malicious_label = np.ones(int(n_samples * 0.2))
    
    df = pd.DataFrame({
        'duration': np.concatenate([normal_duration, malicious_duration]),
        'packet_size': np.concatenate([normal_packet_size, malicious_packet_size]),
        'protocol': np.concatenate([normal_protocol, malicious_protocol]),
        'label': np.concatenate([normal_label, malicious_label])
    })
    return df.sample(frac=1).reset_index(drop=True)

if __name__ == "__main__":
    print("[*] Initializing Machine Learning IDS Pipeline...")
    data = generate_mock_traffic_data(1500)
    
    X = data[['duration', 'packet_size', 'protocol']]
    y = data['label']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("[*] Training Random Forest Classifier Model...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    print("\n=================== IDS EVALUATION REPORT ===================")
    print(f"Model Accuracy Score: {accuracy_score(y_test, predictions) * 100:.2f}%")
    print("\nClassification Matrix:")
    print(classification_report(y_test, predictions, target_names=["Normal Traffic", "Anomaly / Attack"]))
    print("=============================================================")
    
    model_path = os.path.join(os.path.dirname(__file__), "ids_malicious_traffic_model.pkl")
    joblib.dump(model, model_path)
    print(f"\n[+] Success: Trained model serialized and saved to: {model_path}")