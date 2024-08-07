from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Carga del modelo
model = joblib.load('main/RF-V1.0.joblib')

# Inicialización de la aplicación FastAPI
app = FastAPI()

# Definir el modelo de datos
class PredictionRequest(BaseModel):
    Nitrogen: float
    phosphorus: float
    potassium: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

app = FastAPI()

# Ruta raíz
@app.get("/")
async def root():
    return {"message": "Welcome to the crop prediction API!"}

# Ruta para predicción
@app.post("/predict")
def predict(data: PredictionRequest):
    """
    Realiza una predicción del cultivo óptimo basado en las características del suelo y el ambiente.

    Este endpoint recibe un conjunto de características del suelo y del clima, las procesa
    y utiliza un modelo de aprendizaje automático previamente entrenado para predecir el
    cultivo más adecuado para esas condiciones.

    Args:
        data (PredictionRequest): Datos de entrada que contienen las características del suelo y del clima en formato JSON.
            - Nitrogen (float): Nivel de nitrógeno en el suelo.
            - phosphorus (float): Nivel de fósforo en el suelo.
            - potassium (float): Nivel de potasio en el suelo.
            - temperature (float): Temperatura del ambiente en grados Celsius.
            - humidity (float): Humedad relativa del ambiente en porcentaje.
            - ph (float): Nivel de pH del suelo.
            - rainfall (float): Precipitación en mm.
            
            -- e.g: 
            {
            "Nitrogen": 117,
            "phosphorus": 56,
            "potassium": 15,
            "temperature": 25.992374,
            "humidity": 77.054355,
            "ph": 7.368258,
            "rainfall": 89.118821c
            }

    Returns:
        dict: Un diccionario con la predicción del cultivo óptimo.
            - prediction (list): Lista con la predicción del modelo. La lista contiene
              el nombre del cultivo recomendado.
    """
    # Convertir los datos de entrada a un DataFrame de pandas
    df = pd.DataFrame([data.dict()])

    # Realizar la predicción
    prediction = model.predict(df)

    # Devolver la predicción en la respuesta
    return {"prediction": prediction.tolist()}