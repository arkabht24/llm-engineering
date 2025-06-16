import requests
import gradio as gr

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



def chat(user_prompt):
    messages.append({"role": "user", "content": user_prompt})
    print("Messages list ---> ",messages)

    payload_modified = {
        "model": model,
        "messages": messages,
        "stream": False
    }
    message_from_assitant = call_api(payload_modified)
    messages.append({"role":"assistant", "content":message_from_assitant})
    return message_from_assitant


gr.Interface(fn=chat,
             inputs=gr.Textbox(label = "Enter your message"),
             outputs=gr.Markdown(label = "Assistant's response"),
             title="Ollama chatbox by Arka",
             ).launch(share=True)