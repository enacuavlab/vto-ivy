# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(569, 229)
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(410, 10, 141, 191))
        self.label.setPixmap(QtGui.QPixmap(":/images/images/lierre.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(40, 20, 301, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 301, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 341, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(About)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 341, 21))
        self.label_5.setObjectName("label_5")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "Dialog"))
        self.label_2.setText(_translate("About", "Ivy is a software bus provided in LGPL"))
        self.label_3.setText(_translate("About", "http://www2.tls.cena.fr/products/ivy/"))
        self.label_4.setText(_translate("About", "IvyMon Python is a GPL bus viewer (c) Yannick Jestin"))
        self.label_5.setText(_translate("About", "yannick.jestin@enac.fr"))

import ressources_rc
