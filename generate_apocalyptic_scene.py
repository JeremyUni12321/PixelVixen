import apocalypticscene
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

def generate_apocalyptic_scene(width=10, height=5, iterations=3):
    """Simulate Pixel Vixen's iterative 2D art generation process."""
    scene = [[' ' for _ in range(width)] for _ in range(height)]
    for x in range(width):
        if random.random() < 0.5:
            scene[height-1][x] = '█'
    for _ in range(iterations):
        for y in range(height):
            for x in range(width):
                if scene[y][x] == '█' and random.random() < 0.3:
                    if y > 0:
                        scene[y-1][x] = '|'
                elif scene[y][x] == ' ' and random.random() < 0.1:
                    scene[y][x] = '✸'
    return '\n'.join(''.join(row) for row in scene)

def main():
    print("Pixel Vixen's Art Generation (3 Iterations, Text Representation):")
    text_art = generate_apocalyptic_scene()
    print(text_art)

    prompt = "Describe a 2D apocalyptic scene iteratively refined, with jagged ruins and neon flares emerging from a dark base."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
