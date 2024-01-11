from openai import OpenAI

client = OpenAI()


def get_transcribtion(audio_path: str) -> str:
    audio_file = open(audio_path, "rb")
    transcript = client.audio.transcriptions.create(model="whisper-1", file=audio_file)
    return transcript["text"]
