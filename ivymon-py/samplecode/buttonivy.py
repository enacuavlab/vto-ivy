#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from ivy.std_api import IvyInit, IvyStart, IvyBindMsg, IvyStop, IvySendMsg


class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        # un bouton dans une fenêtre
        self.btn = QtWidgets.QPushButton('Button', self)
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.sendTruc)
        self.show()
        # connecté au bus logiciel ivy
        IvyInit('Qt Ivy test', 'Qt Ivy ready')
        IvyBindMsg(self.changeLabel, '^text=(.*)')
        IvyStart("224.255.255.255:2010")

    def sendTruc(self):
        # Qt slot, si on clique sur le bouton, il envoie coucou sur le bus
        IvySendMsg('j ai clique sur el bouton')

    def changeLabel(self, agent, args):
        # Ivy slot: s'il reçoit une message qui va bien, change le bouton
        self.btn.setText(args)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    val = app.exec_()
    IvyStop()
    sys.exit(val)
