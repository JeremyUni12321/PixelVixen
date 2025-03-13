import engine
import requests
import json
import time

API_KEY = "YOUR_API_KEY"  # Replace with your xAI API key
API_URL = "https://api.x.ai/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def generate_art_description(prompt):
    """Generate art description using Grok API."""
    payload = {
        "model": "grok-2-1212",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150,
        "temperature": 0.7
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    return response.json()["choices"][0]["message"]["content"] if response.status_code == 200 else "API Error"

def evolve_art_state(width=12, height=6, stages=3):
    """Generate evolving 2D text art states."""
    art_states = []
    current_state = [[' ' for _ in range(width)] for _ in range(height)]
    
    # Initial state: Sparse ruins
    for x in range(width):
        if random.random() < 0.3:
            current_state[height-1][x] = '█'
    art_states.append('\n'.join(''.join(row) for row in current_state))
    
    # Evolution stages
    for stage in range(stages):
        for y in range(height):
            for x in range(width):
                if current_state[y][x] == '█' and random.random() < 0.4:
                    if y > 0:
                        current_state[y-1][x] = '|'  # Growth upward
                elif current_state[y][x] == ' ' and random.random() < 0.15:
                    current_state[y][x] = '✸'  # Neon emerges
                elif stage > 1 and random.random() < 0.1:
                    current_state[y][x] = '✿'  # Hope appears
        art_states.append('\n'.join(''.join(row) for row in current_state))
    
    return art_states

def main():
    print("Pixel Vixen's Art Evolution Engine")
    print("---------------------------------")
    stages = evolve_art_state()
    for i, stage in enumerate(stages):
        print(f"Stage {i}:")
        print(stage)
        prompt = f"Describe stage {i} of a 2D apocalyptic artwork evolving from sparse ruins to a neon-lit scene with hints of renewal."
        description = generate_art_description(prompt)
        print(f"Description (Grok API): {description}\n")
        time.sleep(1)  # Simulate processing time for dramatic effect

if __name__ == "__main__":
    main()
