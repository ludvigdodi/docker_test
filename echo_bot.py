import requests

TOKEN = "5645942050:AAFeK453jVLJfdAlg2359HR4NYjB2vU9A9Q"
ROOT_URL = f"https://api.telegram.org/bot{TOKEN}"


def get_update(url, update_id):
    responce = requests.get(f"{url}/getUpdates?offset={update_id + 1}")
    return responce.json()


def send_message(chat_id, message_text, url):
    data = {"chat_id": chat_id, "text": message_text}
    responce = requests.post(f"{url}/sendMessage", data=data)


answered_update_id = 0

while True:
    updates = get_update(ROOT_URL, answered_update_id)
    if updates.get("result"):
        update_id = updates.get("result")[0]["update_id"]
        if update_id != answered_update_id:
            chat_id = updates.get("result")[0]["message"]["chat"]["id"]
            message_text = updates.get("result")[0]["message"]["text"]
            send_message(chat_id, message_text, ROOT_URL)
            answered_update_id = update_id

if __name__ == "__main__":
    echo_bot.run(debug=True, host="0.0.0.0", port=5000)
