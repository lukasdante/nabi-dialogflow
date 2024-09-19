from recorder import record_audio
from stt_request import transcribe_audio
from detect_intent import detect_intent_text
from tts_request import init_tts, decode_tts_output, json_write
from play_sound import play_mp3
from dotenv import load_dotenv
import os
import uuid

def record_and_transcribe():
    try:
        # record audio
        record_audio(threshold=1500)

        # transcribe the input audio
        transcribed_audio = transcribe_audio(STT_API_KEY, "output.wav")

        # detect intent from the transcribed audio
        response, parameters = detect_intent_text(transcribed_audio, PROJECT_ID, LOCATION_ID, AGENT_ID, SESSION_ID)
        
        # decode the response to an audio output
        data = json_write(response)
        api_response = init_tts(data)
        decode_tts_output(api_response, "synthesize-text-audio.mp3")
        
        # play the audio output
        play_mp3("synthesize-text-audio.mp3")

        print(parameters)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    load_dotenv()
    STT_API_KEY = os.getenv('STT_API_KEY')
    TTS_API_KEY = os.getenv('TTS_API_KEY')
    PROJECT_ID = os.getenv("DFCX_PROJECT_ID")
    LOCATION_ID = os.getenv("DFCX_LOCATION_ID")
    AGENT_ID = os.getenv("DFCX_AGENT_ID")
    service_account_path = os.getenv("DFCX_SERVICE_ACCOUNT")
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = service_account_path
    
    new_session_id=False
    
    if new_session_id:
        SESSION_ID = uuid.uuid4() 
    else:
        SESSION_ID = "test-session"

    record_and_transcribe()