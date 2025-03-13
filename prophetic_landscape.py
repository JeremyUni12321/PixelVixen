import propheticlandscape
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

def prophetic_landscape(width=12, height=6):
    """Generate a 2D text landscape with apocalyptic warnings and hope."""
    landscape = [[' ' for _ in range(width)] for _ in range(height)]
    for x in range(width):
        if random.random() < 0.2:
            landscape[0][x] = '~'
    water_level = height - 2
    for x in range(width):
        if random.random() < 0.6:
            landscape[water_level][x] = '~'
        if random.random() < 0.3:
            landscape[height-1][x] = '█'
        if random.random() < 0.1:
            landscape[water_level-1][x] = '✿'
    return '\n'.join(''.join(row) for row in landscape)

def main():
    print("Pixel Vixen's Prophetic Landscape (Text Representation):")
    text_art = prophetic_landscape()
    print(text_art)

    prompt = "Describe a 2D prophetic landscape with a flooded city, ruins, and a faint sign of renewal under a stormy sky."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
