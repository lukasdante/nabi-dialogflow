from recorder import record_audio
from stt_request import transcribe_audio
from dfscript import detect_intent_text
from tts_request import init_tts, decode_tts_output, json_write
from play_sound import play_mp3
from dotenv import load_dotenv
import os

def record_and_transcribe():
    try:
        # record audio
        record_audio(threshold=1500)
        # transcribe the input audio
        print("Transcribing audio...")
        transcribed_audio = transcribe_audio(STT_API_KEY, "output.wav")
        # detect intent from the transcribed audio
        response = detect_intent_text(transcribed_audio, PROJECT_ID, LOCATION_ID, AGENT_ID)
        # decode the response to an audio output
        data = json_write(response)
        api_response = init_tts(data)

        decode_tts_output(api_response, "synthesize-text-audio.mp3")
        # TODO: automatically run the audio output
        play_mp3("synthesize-text-audio.mp3")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    load_dotenv()
    STT_API_KEY = os.getenv('STT_API_KEY')
    TTS_API_KEY = os.getenv('TTS_API_KEY')
    PROJECT_ID = os.getenv("DFCX_PROJECT_ID")
    LOCATION_ID = os.getenv("DFCX_LOCATION_ID")
    AGENT_ID = os.getenv("DFCX_AGENT_ID")
    record_and_transcribe()