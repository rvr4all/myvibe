from fastapi import FastAPI
from pydantic import BaseModel
from model.recommender import recommend
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend access (adjust for deployment)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TrackFeatures(BaseModel):
    danceability: float
    energy: float
    valence: float
    tempo: float

@app.post("/recommend")
def get_recommendations(features: TrackFeatures):
    input_vec = [features.danceability, features.energy, features.valence, features.tempo]
    results = recommend(input_vec)
    return results
