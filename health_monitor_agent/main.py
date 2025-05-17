from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from modules.alerts import generate_alerts, generate_explanation
from models import HealthInput

app = FastAPI()

@app.post("/analyze")
async def analyze_health(input: HealthInput):
    alerts = generate_alerts(input.sensor_data, input.environment_data)
    explanation = generate_explanation(alerts, input.dict())
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "alerts": alerts,
        "explanation": explanation
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
