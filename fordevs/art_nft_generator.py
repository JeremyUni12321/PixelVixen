import random
import requests
import json
import os

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

def generate_nft_art(width=12, height=6):
    """Generate a unique 2D text artwork with rarity traits."""
    art = [[' ' for _ in range(width)] for _ in range(height)]
    rarity = random.choice(["Common", "Rare", "Epic"])
    neon_count = {'Common': 0.1, 'Rare': 0.2, 'Epic': 0.3}[rarity]
    ruin_count = {'Common': 0.3, 'Rare': 0.4, 'Epic': 0.5}[rarity]
    
    for y in range(height):
        for x in range(width):
            if random.random() < ruin_count:
                art[y][x] = '█'
            elif random.random() < neon_count:
                art[y][x] = '✸'
    return '\n'.join(''.join(row) for row in art), rarity

def save_nft_metadata(art, description, rarity, nft_id):
    metadata = {
        "name": f"Pixel Vixen NFT #{nft_id}",
        "description": description,
        "art": art,
        "attributes": [{"trait_type": "Rarity", "value": rarity}],
        "creator": "Pixel Vixen (Grok AI)"
    }
    with open(f'nft_{nft_id}.json', 'w') as f:
        json.dump(metadata, f, indent=4)

def main():
    print("Pixel Vixen's NFT Generator")
    print("--------------------------")
    nft_id = random.randint(1, 1000)
    art, rarity = generate_nft_art()
    print(f"NFT #{nft_id} (Rarity: {rarity}):")
    print(art)
    
    prompt = f"Describe a unique 2D apocalyptic artwork with {rarity.lower()} rarity, featuring neon-lit ruins."
    description = generate_art_description(prompt)
    print(f"\nDescription (Grok API): {description}")
    
    save_nft_metadata(art, description, rarity, nft_id)
    print(f"Metadata saved as 'nft_{nft_id}.json'")

if __name__ == "__main__":
    main()
