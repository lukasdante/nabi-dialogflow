from recorder import record_audio
from stt_request import transcribe_audio
from dotenv import load_dotenv
import os

def record_and_transcribe():
    record_audio()
    transcribe_audio(STT_API_KEY,"output.wav")


if __name__ == "__main__":
    load_dotenv()
    STT_API_KEY = os.getenv('STT_API_KEY')
    TTS_API_KEY = os.getenv('TTS_API_KEY')
    record_and_transcribe()

