from chatgpt.meeting_info import ChatGPTHandler
from whisper.transcribtion import get_transcription
import os

AUDIO_DIR = 'audio_files'
NOTES_DIR = '_meeting_notes'
gpt = ChatGPTHandler


def create_meeting_notes(files: list[str]) -> None:
    for filename in files:
        if filename.lower().endswith(('.mp3', '.m4a')):
            create_notes(filename)


def create_notes(filename: str) -> None:
    try:
        transcribtion = get_transcription(os.path.join(AUDIO_DIR, filename))
        info = extract_meeting_details(transcribtion)
        text = format_meeting_notes(info)
        with open(os.path.join(NOTES_DIR, f'{filename}.txt'), 'a') as file:
            file.write(text)
    except Exception as e:
        print(f"Error processing {filename}: {e}")


def format_meeting_notes(info: dict[str, str]) -> str:
    return f'Meeting summary: {info["summary"]} \n\nMeeting notes: \n{info["meeting_notes"]}'


def extract_meeting_details(meeting_text: str) -> dict[str, str]:
    summary = gpt.get_summary(meeting_text)
    notes = gpt.get_notes(meeting_text)
    return {'summary': summary, 'meeting_notes': notes}


def main():
    files = os.listdir(AUDIO_DIR)
    create_meeting_notes(files)


if __name__ == '__main__':
    main()
