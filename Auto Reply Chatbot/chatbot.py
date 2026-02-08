import pyautogui
import time
import pyperclip
from google import genai


pyautogui.click(1060,1056)
time.sleep(1)
pyautogui.click(840,970)
time.sleep(1)

while True:
    pyautogui.moveTo(667,192)
    time.sleep(1)
    pyautogui.dragTo(1881,921,2,button='left')
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.click(956,973)
    text=pyperclip.paste()
    sender=text.split('2026')
    y=sender[-1].split("] ")[-1].split(":")[0]
    time.sleep(2)
    if y=='recipent name':
        client = genai.Client(api_key="Your api key")
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=f"You are Shivang ,you talk in hindi + english, you are given a chat history and based on that reply the sender appropriately : {text}"
        )
        reply=response.text
        pyautogui.click(956,973)
        time.sleep(1)
        pyautogui.write(reply)
        time.sleep(1)
        pyautogui.click(1875,976)