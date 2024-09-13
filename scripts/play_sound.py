from playsound import playsound
import os

def play_mp3(file_path):
    try:
        playsound(file_path)
        print("Playback finished.")
        os.remove(file_path)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'output.mp3' with your actual file path
    mp3_file = 'file_example_MP3_700KB.mp3'
    play_mp3(mp3_file)