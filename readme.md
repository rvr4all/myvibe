# 🎧 MyVibe – Personalized Music Recommender

MyVibe is a lightweight web application that recommends songs based on your input preferences using a machine learning model trained on Spotify track features.

---

## 🔧 Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Frontend     | React + Vite       |
| Backend API  | FastAPI            |
| ML Model     | Scikit-learn (k-NN)|
| Dataset      | Spotify Dataset    |

---

## ⚙️ Features

- 🎶 Recommend songs by adjusting sliders for:
  - Danceability
  - Energy
  - Valence (positivity)
  - Tempo (BPM)
- ⚡ Fast and lightweight backend using FastAPI
- 🎯 ML model trained on Spotify dataset using k-NN
- 🔁 Real-time recommendation updates

---

## 📁 Project Structure

myvibe/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── model/
│   │   ├── train_model.py
│   │   ├── recommender.py
│   │   └── model.pkl               # generated after training
│   └── data/
│       └── spotify_tracks.csv      # downloaded from Kaggle
│
├── frontend/
│   ├── index.html
│   ├── vite.config.js
│   ├── package.json
│   └── src/
│       ├── App.jsx
│       └── main.jsx
│
└── README.md



---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/rvr4ll/myvibe.git
cd myvibe
