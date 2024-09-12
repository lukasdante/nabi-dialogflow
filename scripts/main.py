from recorder import record_audio
from stt_request import transcribe_audio
from dotenv import load_dotenv
import os

def record_and_transcribe():
    record_audio()
    transcribe_audio(API_KEY,"output.wav")


if __name__ == "__main__":
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    record_and_transcribe()

