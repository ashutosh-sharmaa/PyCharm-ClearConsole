#Console Clearing method
def clear_console():
    """This is used to clear console, specifically designed for PyCharm IDE users"""
    import pyautogui
    #print(pyautogui.position())
    pyautogui.moveTo(520,580)
    pyautogui.click()
    pyautogui.hotkey('alt','l')

clear_console()
