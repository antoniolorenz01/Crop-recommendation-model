# Crop Prediction API

## Descripción

Esta API está desarrollada en FastAPI y permite predecir el cultivo óptimo basado en características del suelo y del ambiente. Utiliza un modelo de aprendizaje automático previamente entrenado para hacer recomendaciones de cultivo.

## Estructura del Proyecto

- `server.py`: Contiene la lógica de la aplicación FastAPI, incluyendo la definición de la API y el modelo de datos.
- `Dockerfile`: Define la imagen Docker para la aplicación.
- `requirements.txt`: Lista de dependencias de Python requeridas para ejecutar la aplicación.

## Instalación

Para ejecutar esta API en tu entorno local, sigue estos pasos:

### Requisitos

- Python 3.12.3
- pip

### Paso 1: Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <DIRECTORIO_DEL_REPOSITORIO>
```

### Paso 2: Instalar las dependencias

```bash
pip install -r requirements.txt
```


### Paso 3: Ejecutar la API

```bash
uvicorn server:app --host 0.0.0.0 --port 8000
```
La API estará disponible en http://localhost:8000.


## Uso de la API

#### Endpoints
GET /
Descripción: Devuelve un mensaje de bienvenida.

Respuesta:
{
  "message": "Welcome to the crop prediction API!"
}

POST /predict
Descripción: Realiza una predicción del cultivo óptimo basado en las características del suelo y del ambiente.

Cuerpo de la Solicitud:
{
  "Nitrogen": 117,
  "phosphorus": 56,
  "potassium": 15,
  "temperature": 25.992374,
  "humidity": 77.054355,
  "ph": 7.368258,
  "rainfall": 89.118821
}

Respuesta:
{
  "prediction": ["Cultivo Recomendado"]
}


## Docker
Para ejecutar la API en un contenedor Docker:

### Paso 1: Construir la imagen Docker

```bash
docker build -t crop-prediction-api .
```

### Paso 2: Ejecutar el contenedor Docker
```bash
docker run -p 80:80 crop-prediction-api
```

La API estará disponible en http://localhost.

Dependencias
El archivo requirements.txt contiene las siguientes dependencias:

fastapi
uvicorn
pandas
joblib
pydantic

## Contribuciones
Si deseas contribuir al desarrollo de esta API, por favor, realiza un fork del repositorio y envía un pull request con tus mejoras.

## Licencia
Este proyecto está licenciado bajo la MIT License.

## Contacto
Si tienes alguna pregunta o sugerencia, no dudes en contactarme.