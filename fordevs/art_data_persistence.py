import random
import requests
import json
import sqlite3
from datetime import datetime

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.x.ai/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def generate_art_description(prompt):
    payload = {
        "model": "grok-2-1212",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"] if response.status_code == 200 else "API Error"

def generate_persistent_art(width=12, height=6):
    art = [[' ' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() < 0.4:
                art[y][x] = '█' if random.random() < 0.6 else '✸'
    return '\n'.join(''.join(row) for row in art)

def init_db():
    conn = sqlite3.connect('pixel_vixen_art.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS artworks 
                 (id INTEGER PRIMARY KEY, art TEXT, description TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_art(art, description):
    conn = sqlite3.connect('pixel_vixen_art.db')
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO artworks (art, description, timestamp) VALUES (?, ?, ?)", 
              (art, description, timestamp))
    conn.commit()
    conn.close()

def retrieve_latest_art():
    conn = sqlite3.connect('pixel_vixen_art.db')
    c = conn.cursor()
    c.execute("SELECT art, description, timestamp FROM artworks ORDER BY id DESC LIMIT 1")
    result = c.fetchone()
    conn.close()
    return result if result else ("No art found", "N/A", "N/A")

def main():
    init_db()
    print("Generating and Saving Pixel Vixen's Art...")
    art = generate_persistent_art()
    prompt = "Describe a 2D apocalyptic artwork with neon ruins and sharp lines."
    description = generate_art_description(prompt)
    save_art(art, description)
    
    print("Latest Artwork from Database:")
    latest_art, latest_desc, timestamp = retrieve_latest_art()
    print(f"Art:\n{latest_art}")
    print(f"Description: {latest_desc}")
    print(f"Created: {timestamp}")

if __name__ == "__main__":
    main()
