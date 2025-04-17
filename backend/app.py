from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Optional
from model.recommender import recommend
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the incoming request body format
class RecommendationRequest(BaseModel):
    features: Dict[str, float]
    artist: Optional[str] = None

@app.post("/recommend")
def get_recommendations(request: RecommendationRequest):
    features = request.features
    artist_filter = request.artist

    input_vec = [
        features.get("danceability", 0.5),
        features.get("energy", 0.5),
        features.get("valence", 0.5),
        features.get("tempo", 120),
        features.get("popularity", 50)  # optional, not used by default
    ]

    results = recommend(input_vec, artist_filter=artist_filter)
    return results
