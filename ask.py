
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
        
        print('\n\nResponse: ')
        for chunk in response:
            print(chunk.text, end='')
        print(' \n\n----------------------------------------\n\n')
    


def main():

    import argparse

    parser = argparse.ArguementParser(description="Custom CLI tool for llm usage")

    parser.add_arguement(
        '--no-chat',
        type='bool',
        help='Use for prompting just one message instead of starting a full chat.'
    )

    parser.add_arguement(
        '--file',
        type=argparse.FileType('r', encoding='utf-8'),
        help='Path to a file that is to be given to the model'
    )

    args = parser.parse_args()

    # if args.no_chat:
    #     prompt = " ".join(sys.argv[1:])
    #     one_shot(prompt)

    if not args.no_chat:
        chat_mode()

    else:
        print('Useage: \nOne shot: askai <prompt>\nChat Mode: askai chat')
        

if __name__ == "__main__":
    print('Starting Google AI Studio cli tool')
    client = genai.Client()

    main()
