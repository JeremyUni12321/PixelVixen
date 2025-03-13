import skyline
import requests
import json

API_KEY = "YOUR_API_KEY"  # Replace with your xAI API key
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

def apocalyptic_skyline(width=15, height=5):
    """Generate a 2D text skyline of a crumbling futuristic city."""
    skyline = [[' ' for _ in range(width)] for _ in range(height)]
    base_height = random.randint(1, height-1)
    for x in range(width):
        tower = min(random.randint(0, height), base_height + random.randint(-1, 2))
        for y in range(height-1, height-tower-1, -1):
            skyline[y][x] = '█' if random.random() > 0.2 else '✸'
    skyline[0] = ['~' if random.random() < 0.3 else ' ' for _ in range(width)]
    return '\n'.join(''.join(row) for row in skyline)

def main():
    print("Pixel Vixen's Apocalyptic Skyline (Text Representation):")
    text_art = apocalyptic_skyline()
    print(text_art)

    prompt = "Describe a 2D futuristic skyline of a city in ruin, with jagged towers under a smoky sky, accented by neon flickers."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
