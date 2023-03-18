import gradio as gr
import time
import openai
from gtts import gTTS 
from playsound import playsound 
from datetime import datetime
import os
openai.api_key = "" #input your OPENAI API key here 
messages = [{"role": "system", "content": 'You are a consultant. Respond to all input in 25 words or less.'}]

def transcribe(audio):
    time.sleep(2)
    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    messages.append({"role": "user", "content": transcript["text"]})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    system_message = response["choices"][0]["message"]
    answer = system_message['content']
    var = gTTS(text = answer,lang = "id") 
    current_date_filename = datetime.today().strftime('%Y%m%d%H%M%S') + ".mp3"
    full_file = os.path.dirname(__file__) + current_date_filename
    var.save(full_file)
    playsound(full_file)   
    return "prompt: "+transcript["text"]+"\n answer: "+answer 

ui = gr.Interface(
    fn=transcribe, 
    inputs=[
        gr.Audio(source="microphone", type="filepath")
    ],
    outputs=[
        "textbox"
    ])

ui.launch()
