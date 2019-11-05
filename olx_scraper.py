# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'olxScraper.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import bs4 as bs
import urllib.request
import os
import pyperclip
from lxml import html
import requests


from PyQt5 import QtCore, QtGui, QtWidgets, uic

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('olxScraper.ui', self)
        self.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(10, 0, 562, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setObjectName("lbl_titulo")

        self.btn_dldimages = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dldimages.setGeometry(QtCore.QRect(80, 70, 100, 21))
        self.btn_dldimages.setObjectName("btn_dldimages")
        self.btn_dldimages.clicked.connect(lambda *args : self.dld_images(0))

        self.btn_cpcep = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cpcep.setGeometry(QtCore.QRect(10, 130, 70, 17))
        self.btn_cpcep.setObjectName("btn_cpcep")
        self.btn_cpcep.clicked.connect(lambda *args : self.dld_images(3))

        self.btn_cptitulo = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cptitulo.setGeometry(QtCore.QRect(10, 90, 70, 17))
        self.btn_cptitulo.setObjectName("btn_cptitulo")
        self.btn_cptitulo.clicked.connect(lambda *args : self.dld_images(1))

        self.btn_cpdesc = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cpdesc.setGeometry(QtCore.QRect(10, 110, 70, 17))
        self.btn_cpdesc.setObjectName("btn_cpdesc")
        self.btn_cpdesc.clicked.connect(lambda *args : self.dld_images(2))

        self.btn_cpprice = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cpprice.setGeometry(QtCore.QRect(10, 150, 70, 17))
        self.btn_cpprice.setObjectName("btn_cpprice")
        self.btn_cpprice.clicked.connect(lambda *args : self.dld_images(4))

        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(200, 60, 56, 25))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_clear.clicked.connect(self.clear_entry)

        self.url_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.url_entry.setGeometry(QtCore.QRect(70, 40, 161, 21))
        self.url_entry.setObjectName("url_entry")

        self.lbl_url = QtWidgets.QLabel(self.centralwidget)
        self.lbl_url.setGeometry(QtCore.QRect(35, 40, 21, 16))

        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)

        self.lbl_url.setFont(font)
        self.lbl_url.setObjectName("lbl_url")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 288, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_titulo.setText(_translate("MainWindow", "Seja bem vindo. Cole a URL da OLX no campo:"))
        self.btn_dldimages.setText(_translate("MainWindow", "Download Imagens"))
        self.btn_cpcep.setText(_translate("MainWindow", "CEP"))
        self.btn_cptitulo.setText(_translate("MainWindow", "Titulo"))
        self.btn_cpdesc.setText(_translate("MainWindow", "Descrição"))
        self.btn_cpprice.setText(_translate("MainWindow", "Preço"))
        self.btn_clear.setText(_translate("MainWindow", "Limpar"))
        self.lbl_url.setText(_translate("MainWindow", "Url:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def dld_images(self, el):
        url = self.url_entry.text()
        source = urllib.request.urlopen(url)
        soup = bs.BeautifulSoup(source,'lxml')
        title = soup.find('h1')
        imgs = soup.find_all('img', limit=20)
        desc = soup.find('p')
        ceps = soup.find_all('dd') #Not working yet
        price = soup.find('h2')

        if el == 0:
        #Download IMAGES
            folder = str(title.text)
            os.mkdir(folder)
            for img in imgs:
                url_imagem = img.get('src')
                filename = folder + '/' + str(img.get('alt'))
                #Fazer Download apenas das imagens dos apts.    
                if img.get('alt') != "App Store" and img.get('alt') != "Google Play" and img.get('alt') != "None":
                    imagefile = open(filename + '.jpg', 'wb')
                    imagefile.write(urllib.request.urlopen(url_imagem).read())
                    imagefile.close()
                    #self.url.delete(0, 'end')
                    print('Images downloaded successfully.')

        elif el == 1: #copy Title
            pyperclip.copy(title.text)
            print('Title copied successfully.')

        elif el == 2: #copy Description
            pyperclip.copy(desc.text)
            print('Description copied successfully.')

        elif el == 3: #copy CEP there are many dd's, so when the for find one with length 8, it copies it and the leave the statement
            for cep in ceps:
                if len(cep.get_text()) == 8: 
                    pyperclip.copy(cep.text)
                    break

        elif el == 4: #copy Price
            price_text = price.text[3:8]
            pyperclip.copy(price_text)
            print('Price copied successfully.') #try to copy without the R$


    def clear_entry(self):
        if self.url_entry.text() == '':
            return 
        else:
            self.url_entry.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
