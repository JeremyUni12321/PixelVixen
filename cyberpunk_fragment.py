import cyperpunk
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

def cyberpunk_fragment(width=12, height=5, decay=0.4, neon=0.25):
    """Generate a 2D text fragment of a cyberpunk city with neon decay."""
    city = [['-' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() < decay:
                city[y][x] = ' '
            elif random.random() < neon:
                city[y][x] = '✸'
    city[0] = ['~' if random.random() < 0.3 else ' ' for _ in range(width)]
    return '\n'.join(''.join(row) for row in city)

def main():
    print("Pixel Vixen's Cyberpunk Fragment (Text Representation):")
    text_art = cyberpunk_fragment()
    print(text_art)

    prompt = "Describe a 2D cyberpunk city fragment, neon-lit with decay, sharp lines under a rainy sky."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
