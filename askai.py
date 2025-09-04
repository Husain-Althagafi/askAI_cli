import sys
from google import genai


def stream_reply(prompt, history=None):
    messages = history or []

    messages.append({
        'role': 'user',
        'content': prompt,
    })

    response = client.models.generate_content_stream(
        model = 'gemini-2.5-flash',
        contents = prompt
    )

    for chunk in response:
        print(chunk.text, end="")

    # return {
    #     'role': 'assistant',
    #     'content': full
    # }


def one_shot(prompt):
    stream_reply(prompt)


def chat_mode():
    history = []
    print("Chat mode (type 'exit' to quit)")

    while True:
        prompt = input("You: ")

        if prompt.lower() == 'exit':
            break

        reply = stream_reply(prompt, history=history)

        history.extend([{
            'role': 'user',
            'content': prompt,

        }, reply])

def main():
    if len(sys.argv) > 1 and sys.argv[1] == 'chat':
        chat_mode()

    elif len(sys.argv) > 1:
        prompt = " ".join(sys.argv[1:])
        one_shot(prompt)

    else:
        print('Useage: \nOne shot: askai <prompt>\nChat Mode: askai chat')
        





if __name__ == "__main__":
    print('Starting Google AI Studio cli tool')
    client = genai.Client()

    main()