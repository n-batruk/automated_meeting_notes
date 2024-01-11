from openai import OpenAI

client = OpenAI()


class ChatGPTHandler:
    def __init__(self, meeting_text: str) -> None:
        self.meeting_text = meeting_text

    def get_summary(self) -> str:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": self.meeting_text},
            ],
        )
        return completion["choices"][0]["message"]["content"]

    def get_notes(self) -> str:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": ""},
                {"role": "user", "content": self.meeting_text},
            ],
        )
        return completion["choices"][0]["message"]["content"]
