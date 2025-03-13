from flask import Flask, jsonify, render_template_string
import random
import requests
import json

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.x.ai/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
app = Flask(__name__)

def generate_art_description(prompt):
    payload = {
        "model": "grok-2-1212",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"] if response.status_code == 200 else "API Error"

def generate_gallery_art(width=12, height=6):
    art = [[' ' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() < 0.5:
                art[y][x] = '█' if random.random() < 0.7 else '✸'
    return '\n'.join(''.join(row) for row in art)

@app.route('/')
def gallery():
    art = generate_gallery_art()
    prompt = "Describe a 2D apocalyptic artwork with neon-lit ruins in muted tones."
    description = generate_art_description(prompt)
    html = f"""
    <h1>Pixel Vixen's Web Gallery</h1>
    <pre>{art}</pre>
    <p><strong>Grok Description:</strong> {description}</p>
    <p>Refresh for a new artwork!</p>
    """
    return render_template_string(html)

@app.route('/api/art', methods=['GET'])
def api_art():
    art = generate_gallery_art()
    prompt = "Describe a 2D apocalyptic artwork with neon-lit ruins in muted tones."
    description = generate_art_description(prompt)
    return jsonify({"art": art, "description": description})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
