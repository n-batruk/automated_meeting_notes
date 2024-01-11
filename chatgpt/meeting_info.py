from openai import OpenAI

client = OpenAI()


class ChatGPTHandler:
    def get_summary(meeting_text: str) -> str:
        completion = client.chat.completions.create(
            model='gpt-4',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a meeting expert. You will be given a text of a meeting and you will have to write a summary of it.',
                },
                {'role': 'user', 'content': meeting_text},
            ],
        )
        return completion.choices[0].message.content

    def get_notes(meeting_text: str) -> str:
        completion = client.chat.completions.create(
            model='gpt-4',
            messages=[
                {
                    'role': 'system',
                    'content': 'You are a meeting expert. You will be given a text of a meeting and you will have to write meeting notes. Meeting notes should be in a bullet point format.',
                },
                {'role': 'user', 'content': meeting_text},
            ],
        )
        return completion.choices[0].message.content
