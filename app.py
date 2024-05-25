import openai
import os
from utils import record_audio, play_audio
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable in the .env file")

def main():
    while True:
        record_audio('test.wav')
        with open('test.wav', "rb") as audio_file:
            transcription = openai.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file
            )

        print("Transcription:", transcription.text)

        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are JARVISH, an AI assistant that helps you with your daily tasks."},
                {"role": "user", "content": transcription.text}
            ]
        )

        reply = response.choices[0].message.content
        print("Response:", reply)

        speech_response = openai.audio.speech.create(
            model="tts-1",
            voice="nova",
            input=reply
        )

        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{current_time}.mp3"

        speech_response.stream_to_file(filename)

        play_audio(filename)

if __name__ == "__main__":
    main()
