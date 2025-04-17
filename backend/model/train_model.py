import pandas as pd
from sklearn.neighbors import NearestNeighbors
import pickle
import os

# Load dataset
df = pd.read_csv(os.path.join("..", "data", "spotify_tracks.csv"))

# Select features
features = df[['danceability', 'energy', 'valence', 'tempo']]

# Train model
model = NearestNeighbors(n_neighbors=5)
model.fit(features)

# Save model and dataframe
with open("model.pkl", "wb") as f:
    pickle.dump((model, df), f)

print("Model trained and saved.")
