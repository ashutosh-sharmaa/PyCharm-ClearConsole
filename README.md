# PyCharm-ClearConsole

After installing PyCharm for the first time, noticed there are no built-in methods to clear screen. By taking references from stackoverflow QnA, I've managed to build a function which lets you clear console in PyCharm environment.

You also need to download 'pyautogui' package for this function to be able to work.

pyautogui.size() ==> check you screen size
pyautogui.position() ==> find out the perfect point in the console area where you want to have mouse click.
pyautogui.moveTo(520,580) ==> enter the co-ordinates for a mouse click.
pyautogui.click() ==> mouse click event

Assign HOTKEY using PyCharm preferences for 'clear all'. In my case hotkey for 'clear all' is 'ALT + L'. 

pyautogui.hotkey('alt','l') ==> clears the output window/console.

For any queries, please email me.
