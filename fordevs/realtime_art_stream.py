import random
import requests
import json
import time
import sys

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

def stream_art(width=12, height=6, steps=5):
    """Stream a 2D art generation process in real-time."""
    art = [[' ' for _ in range(width)] for _ in range(height)]
    with open('art_stream.txt', 'w') as f:
        for step in range(steps):
            for y in range(height):
                for x in range(width):
                    if random.random() < 0.3 * (step + 1) / steps:
                        art[y][x] = '█' if random.random() < 0.7 else '✸'
            art_text = '\n'.join(''.join(row) for row in art)
            sys.stdout.write(f"\rStep {step + 1}/{steps}:\n{art_text}\n")
            sys.stdout.flush()
            f.write(f"Step {step + 1}:\n{art_text}\n\n")
            time.sleep(1)  # Simulate real-time generation
    return art_text

def main():
    print("Pixel Vixen's Real-Time Art Stream")
    print("---------------------------------")
    final_art = stream_art()
    prompt = "Describe a 2D apocalyptic artwork emerging in real-time with neon accents and sharp ruins."
    description = generate_art_description(prompt)
    print(f"\nFinal Artwork Description (Grok API): {description}")
    print("Stream saved to 'art_stream.txt'")

if __name__ == "__main__":
    main()
