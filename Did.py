import requests
import time

DID_API_KEY = "cGFsbGlzYWk4ODRAZ21haWwuY29t:sldJ_dmTF1vGKcE87vPHO"  # Replace with your API key
AVATAR_ID = ""  # Replace with your chosen free avatar ID
AUDIO_URL = "https://yourhost.com/output.mp3"  # Replace with your uploaded audio URL

def generate_avatar(AVATAR_ID, AUDIO_URL):
    url = "https://api.d-id.com/talks"
    headers = {
        "Authorization": f"Bearer {DID_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "source_url": AVATAR_ID,
        "script": {"type": "audio", "audio_url": AUDIO_URL},
        "config": {"fluent": True}
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        talk_id = response.json()["id"]
        print(f"✔ Avatar generation started (ID: {talk_id})")
        return talk_id
    else:
        print(" Error:", response.text)
        return None

def check_video_status(talk_id):
    url = f"https://api.d-id.com/talks/{talk_id}"
    headers = {"Authorization": f"Bearer {DID_API_KEY}"}

    while True:
        response = requests.get(url, headers=headers)
        data = response.json()
        if "result_url" in data:
            video_url = data["result_url"]
            print(f"✔ Video Ready: {video_url}")
            return video_url
        else:
            print("⏳ Waiting for video...")
            time.sleep(10)

# Run the process
talk_id = generate_avatar(AVATAR_ID, AUDIO_URL)
if talk_id:
    video_url = check_video_status(talk_id)
    print(f"🔹 Download your video from: {video_url}")
