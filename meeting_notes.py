from openai import OpenAI

def get_meeting_notes(meeting_text):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": ""},
            {"role": "user", "content": meeting_text}
        ]
    )
    return completion['choices'][0]['message']['content']
