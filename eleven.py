import requests

API_KEY = "sk_17f98d862dcf43bc4d94f3546842557e48f18c08e9c0d4f5"
VOICE_ID = "VR6AewLTigWG4xSOukaG"
TEXT = "HHello everyone,I am Sai, and today I’m excited to present my assessment for Pixilia. Pixilia is an innovative platform that focuses on AI-driven creativity, enhancing the way we interact with digital content."

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}

data = {
    "text": TEXT,
    "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    print("Speech saved as output.mp3")
else:
    print(f"Error: {response.status_code}, {response.text}")
