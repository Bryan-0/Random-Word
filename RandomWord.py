from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import *
import random
import sys
import os

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('plugins\\main.ui', self)
        self.setWindowTitle("Random Word")
        self.setWindowIcon(QtGui.QIcon('plugins\\main.ico'))

        self.wordList = []

        self.button = self.findChild(QtWidgets.QPushButton, 'random_btn') # Find the button
        self.button.clicked.connect(self.printButtonPressed)
        self.button2 = self.findChild(QtWidgets.QPushButton, 'load_btn') # Find the button
        self.button2.clicked.connect(self.getfiles)
        self.button3 = self.findChild(QtWidgets.QPushButton, 'save_btn') # Find the button
        self.button3.clicked.connect(self.savefiles)

        self.separate_options = self.findChild(QtWidgets.QComboBox, 'comboBox')

        self.input = self.findChild(QtWidgets.QTextEdit, 'word_holder')
        self.showWord = self.findChild(QtWidgets.QLabel, 'word_selected')
        self.showWord.setStyleSheet("color: red;")

        self.show()


    def separate_words(self, separator):
        self.wordList = list(self.input.toPlainText().split(separator))
        randomIndex = random.randint(0, len(self.wordList) - 1)
        self.showWord.setText(str(self.wordList[randomIndex]))

    def printButtonPressed(self):
        if self.separate_options.currentText() == 'Comma (,)':
            self.separate_words(',')
        elif self.separate_options.currentText() == 'Space ( )':
            self.separate_words(' ')
        elif self.separate_options.currentText() == 'Dot (.)':
            self.separate_words('.')

    def getfiles(self):
        home_dir = os.path.abspath(os.getcwd())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r', encoding='UTF-8')

            with f:
                try:
                     data = f.read()
                except:
                    data = f.read()
                self.input.setText(data)

    def savefiles(self):
        home_dir = os.path.abspath(os.getcwd())
        fname = QFileDialog.getSaveFileName(self, 'Save file', home_dir, '.txt')

        if fname[0]:
            f = open(fname[0]+'.txt', 'w', encoding='UTF-8')

            with f:
                f.write(self.input.toPlainText())

def main(original=Ui):
	app = QtWidgets.QApplication(sys.argv)
	window = original()
	app.exec_()


if __name__ == '__main__':
	main()