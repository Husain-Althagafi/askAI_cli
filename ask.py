import sys
from google import genai

def one_shot(prompt):
    response = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents=[prompt]
    )
    for chunk in response:
        print(chunk.text, end='')

    print(' \n\n--------------------------------------------------------------------------------\n\n') 

def chat_mode(file=None):
    chat = client.chats.create(model='gemini-2.5-flash')

    file_content = file.read() if file else ''

    init_prompt = "You are a helpful AI assistant. You will be provided with a file's content. It may or may not be empty. If not, remember that information incase it is needed. Do not reply to this message at all."
    chat.send_message_stream(init_prompt + file_content)

    while True:
        prompt = input('\n(You): ')

        if prompt == 'exit':
            break

        response = chat.send_message_stream(prompt)

        print(' \n\n--------------------------------------------------------------------------------\n\nResponse: ')
        for chunk in response:
            print(chunk.text, end='')
        print(' \n\n--------------------------------------------------------------------------------\n\n')

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Custom CLI tool for llm usage")

    parser.add_argument('--chat-mode', action='store_true', help='Use for prompting just one message instead of starting a full chat.')
    parser.add_argument('--file', default='./samples/sample.txt', type=argparse.FileType('r', encoding='utf-8'), help='Path to a file that is to be given to the model')

    args = parser.parse_args()

    if not args.chat_mode:  #set as default for now
        print('Chat Mode')
        chat_mode(file=args.file)

    else:
        print('One Run Mode')
        one_shot(' '.join(sys.argv[2:]) if len(sys.argv) > 2 else '')

        # print('Useage: \nOne shot: askai <prompt>\nChat Mode: askai chat')
        
if __name__ == "__main__":
    print('Starting Google AI Studio cli tool')
    client = genai.Client()

    main()
