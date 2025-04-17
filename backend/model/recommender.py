import pickle
import os
from youtubesearchpython import VideosSearch

# Load model and dataframe
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model, df = pickle.load(open(model_path, "rb"))

# Optional: fill missing artist values
df["artists"] = df["artists"].fillna("Unknown Artist")


# Get YouTube embed URL for a song query
def get_first_video_embed_url(query):
    try:
        search = VideosSearch(query, limit=1)
        result = search.result()
        video_id = result["result"][0]["id"]
        return f"https://www.youtube.com/embed/{video_id}"
    except Exception:
        return None


# Main recommendation function
def recommend(input_features, artist_filter=None):
    results = []

    # ✅ Artist-only search — limit to top 5 results to improve performance
    if artist_filter:
        count = 0
        for _, row in df.iterrows():
            if count >= 5:
                break

            artist_value = row.get("artists")
            if not isinstance(artist_value, str):
                continue

            if artist_filter.lower() in artist_value.lower():
                title = f"{row['track_name']} {artist_value}"
                embed_url = get_first_video_embed_url(title)

                results.append({
                    "track_name": row['track_name'],
                    "artist": artist_value,
                    "youtube_embed_url": embed_url
                })
                count += 1

        return results

    # Default model-based recommendation
    distances, indices = model.kneighbors([input_features])
    for i in indices[0]:
        row = df.iloc[i]
        artist_value = row.get("artists", "Unknown Artist")
        title = f"{row['track_name']} {artist_value}"
        embed_url = get_first_video_embed_url(title)

        results.append({
            "track_name": row['track_name'],
            "artist": artist_value,
            "youtube_embed_url": embed_url
        })

    return results
