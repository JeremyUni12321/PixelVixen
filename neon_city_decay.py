import neoncity
import requests
import json

# Grok API configuration
API_KEY = "YOUR_API_KEY"  # Replace with your xAI API key
API_URL = "https://api.x.ai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def generate_art_description(prompt):
    """Use Grok API to generate a description of Pixel Vixen's art."""
    payload = {
        "model": "grok-2-1212",  # Use the latest model as of March 2025
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.text}"

def neon_city_decay(width=12, height=6, decay_rate=0.5):
    """Generate a 2D text representation of a decaying neon city."""
    city = [['█' for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            if random.random() < decay_rate:
                city[y][x] = ' '  # Ruined areas
            elif random.random() < 0.15:
                city[y][x] = '✸'  # Neon sparks
    return '\n'.join(''.join(row) for row in city)

def main():
    # Generate text-based art
    print("Pixel Vixen's Neon Decay (Text Representation):")
    text_art = neon_city_decay()
    print(text_art)

    # Use Grok API to generate a detailed art description
    prompt = "Describe a 2D apocalyptic artwork of a neon-lit city crumbling under its own excess, with sharp lines and muted grays pierced by electric hues."
    description = generate_art_description(prompt)
    print("\nPixel Vixen's Artistic Vision (Grok API):")
    print(description)

    # Placeholder for image generation (future Aurora API integration)
    # image_prompt = "A neon-lit city crumbling, sharp 2D lines, muted grays with pink and blue neon accents"
    # image = generate_image(image_prompt)  # Uncomment when Aurora API is available
    # print("Image generated and saved as 'neon_city_decay.jpg'")

if __name__ == "__main__":
    main()
