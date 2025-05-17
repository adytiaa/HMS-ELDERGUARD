from pydantic import BaseModel
from typing import Optional

class SensorData(BaseModel):
    heart_rate: float
    hrv: float
    blood_sugar: float
    acceleration: float

class EnvironmentData(BaseModel):
    aqi: float
    temperature: float
    humidity: float
    pm25: Optional[float] = None
    ozone: Optional[float] = None
    co: Optional[float] = None

class HealthInput(BaseModel):
    sensor_data: SensorData
    environment_data: EnvironmentData

class ExplanationRequest(BaseModel):
    alerts: list[str]
    context: HealthInput
