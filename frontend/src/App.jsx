import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [features, setFeatures] = useState({
    danceability: 0.5,
    energy: 0.5,
    valence: 0.5,
    tempo: 120,
    popularity: 50,
  });
  const [artistName, setArtistName] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [selectedUrl, setSelectedUrl] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFeatures({ ...features, [name]: parseFloat(value) });
  };

  const getRecommendations = async () => {
    const payload = {
      features,
      artist: artistName
    };
    const res = await axios.post("http://localhost:8000/recommend", payload);
    setRecommendations(res.data);
  };

  return (
    <div style={{ display: "flex", padding: "2rem" }}>
      {/* Left side: Sliders + Song list */}
      <div style={{ width: "50%", paddingRight: "2rem" }}>
        <h2>🎵 MyVibe Recommender</h2>

        {/* Feature sliders */}
        {Object.entries(features).map(([key, value]) => (
          <div key={key} style={{ marginBottom: "1rem" }}>
            <label>{key}: {value}</label><br />
            <input
              type="range"
              name={key}
              min={key === "tempo" ? 60 : key === "popularity" ? 0 : 0}
              max={key === "tempo" ? 200 : key === "popularity" ? 100 : 1}
              step={key === "tempo" || key === "popularity" ? 1 : 0.01}
              value={value}
              onChange={handleChange}
              style={{ width: "100%" }}
            />
          </div>
        ))}

        {/* Artist name input */}
        <div style={{ marginBottom: "1rem" }}>
          <label>Artist Name:</label><br />
          <input
            type="text"
            value={artistName}
            onChange={(e) => setArtistName(e.target.value)}
            placeholder="e.g. Dua Lipa"
            style={{ width: "100%", padding: "0.5rem" }}
          />
        </div>

        <button onClick={getRecommendations}>Recommend Songs</button>

        <h3>Recommendations</h3>
        {recommendations.map((song, idx) => (
          <div key={idx} style={{ marginBottom: "1rem" }}>
            <p><strong>{song.track_name}</strong> – {song.artist}</p>
            <button
              onClick={() => setSelectedUrl(song.youtube_embed_url)}
              style={{ background: "none", border: "none", color: "blue", cursor: "pointer" }}
            >
              ▶️ Preview
            </button>
          </div>
        ))}
      </div>

      {/* Right side: iframe preview */}
      <div style={{ width: "50%" }}>
        <h3>🎬 YouTube Preview</h3>
        {selectedUrl ? (
          <iframe
            width="100%"
            height="315"
            src={selectedUrl}
            title="YouTube Preview"
            frameBorder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          ></iframe>
        ) : (
          <p>No song selected</p>
        )}
      </div>
    </div>
  );
}
