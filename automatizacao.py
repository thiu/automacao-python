import pyautogui
import time
import pandas as pd

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.PAUSE = 0.5

pyautogui.hotkey('command', 'space', interval=0.5)

pyautogui.write('chrome') 
pyautogui.press('enter')

time.sleep(3)

pyautogui.write(link) 
pyautogui.press('enter') 

time.sleep(3)

pyautogui.click(x=722, y=440)

pyautogui.write('login')
pyautogui.press('tab')
pyautogui.write('senha muito dificil de decorar')
pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

produtos = pd.read_csv('produtos.csv')

pyautogui.press('tab') 
    
for produto in produtos.index:
    pyautogui.write(str(produtos.loc[produto, 'codigo']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[produto, 'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[produto, 'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[produto, 'categoria']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[produto, 'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(produtos.loc[produto, 'custo']))
    pyautogui.press('tab')
    if(str(produtos.loc[produto, 'obs']) != 'nan'):
        pyautogui.write(str(produtos.loc[produto, 'obs']))
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(50000)
    pyautogui.click(x=722, y=322)