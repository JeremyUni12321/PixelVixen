import vignette
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

def apocalyptic_vignette(width=12, height=6):
    """Generate a 2D text vignette of an apocalyptic scene with neon echoes."""
    scene = [[' ' for _ in range(width)] for _ in range(height)]
    horizon = height - 2
    scene[horizon] = ['=' if random.random() < 0.7 else ' ' for _ in range(width)]
    figure_x = random.randint(2, width-3)
    scene[horizon-1][figure_x] = '▲'
    for y in range(horizon):
        for x in range(width):
            if random.random() < 0.1:
                scene[y][x] = '✸'
    for x in range(width):
        if random.random() < 0.3:
            scene[horizon+1][x] = '█'
    return '\n'.join(''.join(row) for row in scene)

def main():
    print("Pixel Vixen's Apocalyptic Vignette (Text Representation):")
    text_art = apocalyptic_vignette()
    print(text_art)

    prompt = "Describe a 2D apocalyptic vignette with a lone figure against a fiery horizon, neon sparks, and rubble below."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
