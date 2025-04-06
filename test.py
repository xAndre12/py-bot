import pyautogui
import time
import threading
import math
import random

# time.sleep(2)
# print(pyautogui.position())
pyautogui.moveTo(1129,485,1)

a = True
x=0

def autoIncrement(increment):
    while True:
        data['cookie'] = data['cookie'] + increment
        time.sleep(1)

def runAction(action, param):
    thread = threading.Thread(target=action, args=(param,))
    thread.daemon = True  
    thread.start()

data = {
    'cookie' : 0,
    'currentBuy': 'cursor',
    'cursor': {
        'buy': 15,
        'moveTo': {
            'x': 1813,
            'y': 634
        },
        'next' : 'granny',
        'incrementCookie': 0.1,
        'action':autoIncrement,
        'stopBuy': {
            'items': random.randint(2, 5),
            'firstBuy': 15,
            'totalItems': 0
        }
    },
    'granny':{
        'buy':100,
        'moveTo': { 
            'x':1761,
            'y':707
        },
        'next': 'farm',
        'incrementCookie': 1,
        'action':autoIncrement,
        'stopBuy': {
            'items': random.randint(2, 5),
            'firstBuy': 100,
            'totalItems': 0
        }
    },
    'farm':{
        'buy': 1100,
        'moveTo': {
            'x': 1757,
            'y': 775
        },
        'next': 'cursor',
        'incrementCookie': 8,
        'action':autoIncrement,
        'stopBuy': {
            'items': random.randint(2, 5),
            'firstBuy': 1100,
            'totalItems': 0
        }
    }
}

def advancedBuy():
    global x
    while data[data['currentBuy']]['stopBuy']['items'] != data[data['currentBuy']]['stopBuy']['totalItems']:
        pyautogui.click()
        x= x + 1
        if (x + data['cookie']) >= data[data['currentBuy']]['buy']:
            pyautogui.moveTo(data[data['currentBuy']]['moveTo']['x'],data[data['currentBuy']]['moveTo']['y'],1)
            pyautogui.click() 
            x= x - data[data['currentBuy']]['buy']
            data[data['currentBuy']]['buy'] = math.ceil(data[data['currentBuy']]['buy'] * 1.15)
            runAction(data[data['currentBuy']]['action'], data[data['currentBuy']]['incrementCookie'])
            pyautogui.moveTo(1129,485,1)
            data[data['currentBuy']]['stopBuy']['totalItems'] = data[data['currentBuy']]['stopBuy']['totalItems'] + 1



while a == True:
    pyautogui.click()
    x = x + 1
    print(x + data['cookie'])
    if (x + data['cookie']) >= data[data['currentBuy']]['buy']:
        a = False
        firstBuy = data[data['currentBuy']]['buy'] 
        pyautogui.moveTo(data[data['currentBuy']]['moveTo']['x'],data[data['currentBuy']]['moveTo']['y'],1)
        pyautogui.click()
        x= x - data[data['currentBuy']]['buy']
        data[data['currentBuy']]['buy'] = math.ceil(data[data['currentBuy']]['buy'] * 1.15)
        runAction(data[data['currentBuy']]['action'], data[data['currentBuy']]['incrementCookie'])
        pyautogui.moveTo(1129,485,1)
        if data[data['currentBuy']]['stopBuy']['firstBuy'] != firstBuy:
            advancedBuy()
            data['currentBuy'] = data[data['currentBuy']]['next']
            a = True
        if data[data['currentBuy']]['stopBuy']['firstBuy'] == firstBuy:
             data['currentBuy'] = data[data['currentBuy']]['next']
             a = True

                
    


    

