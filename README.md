#kraigerf: AI Voice Assistant using GPT-4o

Voice-activated assistant using OpenAI's Whisper, GPT-4o, and Text-to-Speech API
Features:

    Record audio input from the user
    Transcribe recorded audio to text using OpenAI's Whisper model
    Generate a response using OpenAI's GPT-4o model
    Convert the generated response to speech
    Play the generated speech response to the user

Usage:

To use the voice assistant, simply run the main.py script. The system will prompt you to speak, record your input, transcribe it, generate a response, and then play the response back to you.
Dependencies:

    Python 3.7 or higher
    OpenAI's openai Python package
    python-dotenv for managing environment variables
    sounddevice for audio recording
    scipy for handling audio data
    pygame for audio playback
    numpy for numerical operations

To install the required libraries, run:

bash

pip install -r requirements.txt

Installation

    Clone the repository

    bash

git clone https://github.com/mattaldi/kraigerf.git
cd kraigerf

Install the required libraries

bash

pip install -r requirements.txt

Create a .env file in the root directory and add your OpenAI API key

makefile

OPENAI_API_KEY=your_openai_api_key_here

Run the main script

bash

    python main.py

Contributing:

If you would like to contribute to this project, please submit a pull request with your proposed changes.
License:

This project is licensed under the MIT License.

Have fun interacting with Kraigerf, your AI voice assistant!
