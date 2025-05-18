# health_monitor_agent/modules/alerts.py

from models import SensorData, EnvironmentData
import requests
import os
import google.generativeai as genai

# Set Gemini API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

COPERNICUS_ENDPOINT = "https://api.openaq.org/v2/latest"  # Example public air quality API

def fetch_copernicus_data(location="London"):
    params = {"city": location, "limit": 1}
    response = requests.get(COPERNICUS_ENDPOINT, params=params)
    data = response.json()
    try:
        measurements = {m["parameter"]: m["value"] for m in data["results"][0]["measurements"]}
        return {
            "aqi": measurements.get("pm10", 50),
            "pm25": measurements.get("pm25", 12),
            "ozone": measurements.get("o3", 20),
            "co": measurements.get("co", 0.4)
        }
    except (KeyError, IndexError):
        return {"aqi": 50, "pm25": 12, "ozone": 20, "co": 0.4}

def predict_heart_attack(data: SensorData):
    if data.heart_rate > 100 and data.hrv < 50:
        return "high"
    return "low"

def predict_blood_sugar_trend(data: SensorData):
    if data.blood_sugar > 180:
        return "rising"
    return "stable"

def detect_fall(data: SensorData):
    if abs(data.acceleration) > 20:
        return True
    return False

def assess_environment_risk(env: EnvironmentData):
    if env.aqi > 100 or (env.pm25 and env.pm25 > 35):
        return "moderate"
    return "low"

def generate_alerts(data: SensorData, env: EnvironmentData):
    heart_risk = predict_heart_attack(data)
    sugar_trend = predict_blood_sugar_trend(data)
    fall = detect_fall(data)
    env_risk = assess_environment_risk(env)

    alerts = []
    if heart_risk == "high":
        alerts.append("⚠️ Risk of cardiac stress detected. Seek medical advice if symptoms worsen.")
    if sugar_trend == "rising":
        alerts.append("🩸 Blood sugar is rising. Consider checking insulin or food intake.")
    if fall:
        alerts.append("🚨 Fall detected. Emergency contact may be needed.")
    if env_risk == "moderate":
        alerts.append("🌫️ Air quality is moderate. Stay indoors if possible.")

    return alerts

def generate_explanation(alerts: list[str], context: dict):
    prompt = (
        f"You are a health assistant. Based on the following alerts and patient data, explain in plain language:\n"
        f"Alerts: {alerts}\n"
        f"Heart Rate: {context['sensor_data'].heart_rate}, HRV: {context['sensor_data'].hrv},\n"
        f"Blood Sugar: {context['sensor_data'].blood_sugar}, Acceleration: {context['sensor_data'].acceleration},\n"
        f"AQI: {context['environment_data'].aqi}, PM2.5: {context['environment_data'].pm25}"
    )
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text
