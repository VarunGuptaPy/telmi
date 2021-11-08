from googletrans import Translator
import keyboard 
from pyautogui import hotkey
from pyperclip import *
from bs4 import BeautifulSoup
from datetime import date
import time
from PyQt5 import *
from PyQt5.QtCore import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from wordsss import *
import os
class gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

def copy():
    hotkey('ctrl','c')
    time.sleep(.03)
    value = paste()
    return value
def translate():
    dates = date.today()
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('i'):            
        time.sleep(.03)
        # url = f'https://www.wordhippo.com/what-is/sentences-with-the-word/{str(value)}.html'
        # content = requests.get(url)
        # html = content.content
        # soup = BeautifulSoup(html,'html.parser')
        # sentences = soup.find_all('td',id="exv2st29172866")
        # print(sentences)
        a = copy()
        Guiapp = QApplication(sys.argv)
        jarvis_gui = gui_start()
        jarvis_gui.show()
        gui = jarvis_gui.gui
        # gui.label.setText(a)
        gui.label.setText(a)
        translator = Translator()
        text = translator.translate(a,dest='hi',src='en')
        gui.label_3.setText(text.text)
        # self.label.setText(text.text)

        def fileconvert():
            files = os.listdir()
            if f'{dates}.txt' in files:
                file = open(f'word_{dates}.txt','a',encoding='utf-8')
                file.writelines(f'{a} -----> {text.text}\n')
                file.close()
            else:
                file = open(f'word_{dates}.txt','a',encoding='utf-8')
                file.writelines(f'{a} -----> {text.text}\n')
                file.close()
        gui.pushButton.clicked.connect(fileconvert)
        Guiapp.exec_()
        Guiapp.quit()

        
if __name__ == '__main__':
    while True:
        translate()     
