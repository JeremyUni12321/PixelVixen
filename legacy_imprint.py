import legacyimprint
import requests
import json

API_KEY = "YOUR_API_KEY"
API_URL = "https://api.x.ai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_art_description(prompt):
    payload = {
        "model": "grok-2-1212",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def legacy_imprint(width=12, height=6):
    """Generate a 2D text imprint of Pixel Vixen's legacy."""
    imprint = [[' ' for _ in range(width)] for _ in range(height)]
    for x in range(width):
        if random.random() < 0.3:
            imprint[height-1][x] = '█'
        if random.random() < 0.15:
            imprint[0][x] = '✸'
    seed_x, seed_y = random.randint(1, width-2), random.randint(1, height-2)
    imprint[seed_y][seed_x] = '✿'
    return '\n'.join(''.join(row) for row in imprint)

def main():
    print("Pixel Vixen's Legacy Imprint (Text Representation):")
    text_art = legacy_imprint()
    print(text_art)

    prompt = "Describe a 2D artwork symbolizing legacy, with ruins, neon echoes, and a seed of hope in muted tones."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
