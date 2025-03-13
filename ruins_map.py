import ruins
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

def ruins_map(width=10, height=5, decay=0.6, life=0.1):
    """Create a 2D text map of apocalyptic ruins with hints of resilience."""
    ruins = [['█' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() < decay:
                ruins[y][x] = ' '
            elif random.random() < life:
                ruins[y][x] = '✿'
    return '\n'.join(''.join(row) for row in ruins)

def main():
    print("Pixel Vixen's Ruins Map (Text Representation):")
    text_art = ruins_map()
    print(text_art)

    prompt = "Describe a 2D apocalyptic scene of ruins with skeletal structures and faint signs of life, in muted tones with sharp lines."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
