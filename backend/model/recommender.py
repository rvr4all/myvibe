import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model, df = pickle.load(open(model_path, "rb"))

# def recommend(input_features):
#    distances, indices = model.kneighbors([input_features])
 #   recommendations = df.iloc[indices[0]][['track_name', 'artists']]
#    return recommendations.to_dict(orient="records")
from youtubesearchpython import VideosSearch

def recommend(input_features):
    distances, indices = model.kneighbors([input_features])
    results = []

    for i in indices[0]:
        row = df.iloc[i]
        query = f"{row['track_name']} {row['artists']}"

        # search YouTube for video
        video_search = VideosSearch(query, limit=1)
        search_result = video_search.result()
        video_id = search_result['result'][0]['id'] if search_result['result'] else None
        youtube_embed_url = f"https://www.youtube.com/embed/{video_id}" if video_id else None

        results.append({
            "track_name": row['track_name'],
            "artist": row['artists'],
            "youtube_embed_url": youtube_embed_url
        })

    return results


