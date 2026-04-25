import os
import requests

TOKEN = os.environ["RUBIKA_TOKEN"]
offset = None

while True:
    url = f"https://botapi.rubika.ir/v3/{TOKEN}/getUpdates"
    payload = {"limit": 10}
    if offset:
        payload["offset_id"] = offset
    resp = requests.post(url, json=payload).json()
    
    if resp.get("status") == "OK":
        updates = resp["data"]["updates"]
        for upd in updates:
            # process each update (e.g., respond to /start)
            if upd["type"] == "NewMessage":
                chat_id = upd["chat_id"]  # or upd["new_message"]["sender_id"]
                # reply logic here...
        # update offset for next run
        if updates:
            offset = resp["data"]["next_offset_id"]
    else:
        break
    # Short sleep to avoid hitting rate limits, but remember GitHub Actions timeout!
    # For a scheduled run, you can just process once and exit.
