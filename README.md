# 🩺 Health Monitor Agent

An AI-powered health monitoring system powered by sensor data, Copernicus environmental insights, and Google Gemini LLM for early warning and natural language explanations of potential health risks.

## 🚀 Features

- 🫀 **Heart Attack Risk Detection** – Uses heart rate and HRV data.
- 🩸 **Blood Sugar Trend Monitoring** – Detects elevated blood sugar patterns.
- 🛑 **Fall Detection** – Identifies dangerous acceleration events.
- 🌫️ **Environmental Risk Awareness** – Integrates air quality data from Copernicus (via OpenAQ).
- 🤖 **LLM-based Explanations** – Summarizes alerts in user-friendly language using Gemini Pro.

## 🧠 Powered by
- **Google Gemini API** for natural language generation
- **OpenAQ API** for public air quality data
- **FastAPI** for backend endpoints

## 🛠️ Setup

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/health-monitor-agent.git
cd health-monitor-agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Your API Key
```bash
export GEMINI_API_KEY="your_gemini_api_key"
```

### 4. Run the API
```bash
uvicorn health_monitor_agent.main:app --reload
```

## 📡 API Endpoint

### `POST /analyze`

#### Request Body
```json
{
  "sensor_data": {
    "heart_rate": 105,
    "hrv": 42,
    "blood_sugar": 185,
    "acceleration": 22.5
  },
  "environment_data": {
    "aqi": 120,
    "temperature": 30,
    "humidity": 60,
    "pm25": 40,
    "ozone": 30,
    "co": 0.5
  }
}
```

#### Response
```json
{
  "timestamp": "2025-05-17T10:45:00Z",
  "alerts": [
    "⚠️ Risk of cardiac stress detected. Seek medical advice if symptoms worsen.",
    "🩸 Blood sugar is rising. Consider checking insulin or food intake.",
    "🚨 Fall detected. Emergency contact may be needed.",
    "🌫️ Air quality is moderate. Stay indoors if possible."
  ],
  "explanation": "Based on your data, there are signs of elevated cardiovascular stress..."
}
```

## 📂 Project Structure

```
health_monitor_agent/
├── modules/
│   └── alerts.py
├── models.py
├── main.py
requirements.txt
README.md
```

## 🧪 Testing

You can use Postman or `curl` to test the `/analyze` endpoint with sample payloads.

---
## Architecture

┌────────────────────┐
│ Wearable Sensors   │ ◄────── ECG, HR, BP, Glucose, Motion
└────────┬───────────┘
         │
         ▼
┌────────────────────┐
│ Data Preprocessing │ ◄──── Clean, Normalize, Feature Extract
└────────┬───────────┘
         │
         ▼
┌────────────────────┐       ┌──────────────────────┐
│ ML Risk Detection  │◄─────▶│ Copernicus Data Fetch│ ◄── Air Quality, Weather
│ (Heart/Fall/Sugar) │       └──────────────────────┘
└────────┬───────────┘
         │
         ▼
┌────────────────────────┐
│ LLM Agent (e.g., GPT)  │ ◄── Prompt with risks + environment
│ - Analyze + Summarize  │
│ - Explain Risk         │
│ - Recommend Actions    │
└────────┬───────────────┘
         │
         ▼
┌────────────────────┐
│ Alert System       │ ◄──── App, SMS, Caregiver Dashboard
└────────────────────┘

## 📃 License

MIT License
