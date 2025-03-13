import circuit
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

def circuit_grid(width=10, height=5, decay=0.5, neon=0.2):
    """Generate a 2D text grid of a decaying circuit with neon highlights."""
    grid = [['|' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() < decay:
                grid[y][x] = ' '
            elif random.random() < neon:
                grid[y][x] = '*'
    return '\n'.join(''.join(row) for row in grid)

def main():
    print("Pixel Vixen's Circuit Grid (Text Representation):")
    text_art = circuit_grid()
    print(text_art)

    prompt = "Describe a 2D artwork of a decaying circuit grid, sharp lines in muted grays with neon flares cutting through."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

if __name__ == "__main__":
    main()
