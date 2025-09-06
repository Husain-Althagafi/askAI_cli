Made this because my laptop is insanely slow and last time in network security we had to open an llm to ask it a question and it took a very long time to just open the tab. Then each time I typed something it took several minutes just to let me enter the prompt. So i decided to just make a cli tool so i wouldnt have to deal with the web issues. There are existing ones but i figured I may aswell make my own so I did that.

To use this here are the steps:

1. clone the repo
2. install requirements from requirements.txt (use uv its goated
3. activate venv
4. run: pyinstaller --onefile ask.py
5. this will generate a dist file. inside it will be the ask.exe. Just include this in your PATH and ur good.

Thx for reading. if ur laptop is slow aswell hope this will be useful. Ill try to add actual features to it so that there is a point to using this instead of just the existing cli from google. 
