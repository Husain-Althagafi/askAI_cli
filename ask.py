
import sys
from google import genai

def one_shot(prompt):
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=[prompt]
    )
    for chunk in response:
        print(chunk.text, end='')

        

def chat_mode():
    chat = client.chats.create(model='gemini-2.5-flash')

    while True:
        prompt = input('\n(You): ')

        if prompt == 'exit':
            break

        response = chat.send_message_stream(prompt)

        for chunk in response:
            print(chunk.text, end='')
    


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
