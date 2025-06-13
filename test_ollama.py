import requests
import json

OLLAMA_URL = "http://localhost:11434/api/chat"

model = "llama3.2"

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
  ]




def call_api(payload_modified):
    response = requests.post(OLLAMA_URL,json=payload_modified)
    if response.status_code == 200:
        data = response.json()
        print("Response from Ollama:")
        if "message" in data and "content" in data["message"]:
            print(data["message"]["content"])
            return data["message"]["content"]
        else:
            print("No body found")
            return ""

    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return ""


def return_user_prompt():
    user_prompt = str(input("Enter your prompt : "))
    return user_prompt



ctr = 1
while ctr <=3:
    user_prompt = return_user_prompt()
    messages.append({"role": "user", "content": user_prompt})
    print("Messages list ---> ",messages)

    payload_modified = {
        "model": model,
        "messages": messages,
        "stream": False
    }
    message_from_assitant = call_api(payload_modified)
    messages.append({"role":"assistant", "content":message_from_assitant})
    ctr+=1
