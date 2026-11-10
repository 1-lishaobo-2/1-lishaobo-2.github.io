#pip install pyautogui  操作界面和鼠标
#pip install pyperclip  操作剪贴板
import pyperclip
import pyautogui
pyautogui.moveTo(x=940,y=730)
pyautogui.click()
for i in range(50):
  pyperclip.copy('乐乐')
  pyautogui.hotkey('ctrl', 'v')
  pyautogui.press('enter')




