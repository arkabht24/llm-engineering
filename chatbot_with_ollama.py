
import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/chat"
model = "llama3.2"

SYSTEM_PROMPT = {"role":"system","content": "You are a helpful assistant."}



def call_api(messages):
    payload = {
        "model":model,
        "messages":messages,
        "stream": False
    }
    response = requests.post(OLLAMA_URL,json=payload)
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
    

def chat(user_input,chat_history):
    if chat_history is None:
        chat_history = []
    messages = [SYSTEM_PROMPT]

    for user_message, assistant_message in chat_history:
        messages.append({"role":"user","content":user_message})
        messages.append({"role":"assistant","content":assistant_message})
    
    messages.append({"role":"user","content":user_input})


    assistant_message_current = call_api(messages)

    return assistant_message_current


gr.ChatInterface(chat).launch()
