# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_new.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(946, 556)
        Main.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.frame_5 = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.autoScroll = QtWidgets.QCheckBox(self.frame_5)
        self.autoScroll.setChecked(True)
        self.autoScroll.setObjectName("autoScroll")
        self.horizontalLayout_4.addWidget(self.autoScroll)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.messages = QtWidgets.QTextEdit(self.frame_5)
        self.messages.setReadOnly(True)
        self.messages.setObjectName("messages")
        self.verticalLayout_8.addWidget(self.messages)
        self.frame_6 = QtWidgets.QFrame(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.events = QtWidgets.QTextEdit(self.frame_6)
        self.events.setReadOnly(True)
        self.events.setObjectName("events")
        self.verticalLayout_9.addWidget(self.events)
        self.horizontalLayout_7.addWidget(self.splitter_2)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuBus = QtWidgets.QMenu(self.menubar)
        self.menuBus.setObjectName("menuBus")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.idDock = QtWidgets.QDockWidget(Main)
        self.idDock.setObjectName("idDock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.busLabel = QtWidgets.QLabel(self.frame_3)
        self.busLabel.setObjectName("busLabel")
        self.horizontalLayout_5.addWidget(self.busLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.nameLabel = QtWidgets.QLabel(self.frame_3)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_6.addWidget(self.nameLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.dockWidgetContents)
        self.frame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.msg = QtWidgets.QComboBox(self.frame_4)
        self.msg.setEditable(True)
        self.msg.setObjectName("msg")
        self.horizontalLayout_3.addWidget(self.msg)
        self.sendButton = QtWidgets.QPushButton(self.frame_4)
        self.sendButton.setObjectName("sendButton")
        self.horizontalLayout_3.addWidget(self.sendButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.frame_2 = QtWidgets.QFrame(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.agentList = QtWidgets.QListWidget(self.frame_2)
        self.agentList.setObjectName("agentList")
        self.verticalLayout_2.addWidget(self.agentList)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.killButton = QtWidgets.QPushButton(self.frame_2)
        self.killButton.setObjectName("killButton")
        self.horizontalLayout.addWidget(self.killButton)
        self.inspectButton = QtWidgets.QPushButton(self.frame_2)
        self.inspectButton.setObjectName("inspectButton")
        self.horizontalLayout.addWidget(self.inspectButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.idDock.setWidget(self.dockWidgetContents)
        Main.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.idDock)
        self.bindDock = QtWidgets.QDockWidget(Main)
        self.bindDock.setObjectName("bindDock")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.dockWidgetContents_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame = QtWidgets.QFrame(self.dockWidgetContents_3)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.bindList = QtWidgets.QListWidget(self.frame)
        self.bindList.setObjectName("bindList")
        self.verticalLayout_6.addWidget(self.bindList)
        self.removeButton = QtWidgets.QPushButton(self.frame)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout_6.addWidget(self.removeButton)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newBinding = QtWidgets.QComboBox(self.frame)
        self.newBinding.setEditable(True)
        self.newBinding.setObjectName("newBinding")
        self.horizontalLayout_2.addWidget(self.newBinding)
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_2.addWidget(self.addButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.removeButton.raise_()
        self.bindList.raise_()
        self.verticalLayout_7.addWidget(self.frame)
        self.bindDock.setWidget(self.dockWidgetContents_3)
        Main.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.bindDock)
        self.actionQuit = QtWidgets.QAction(Main)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCredits = QtWidgets.QAction(Main)
        self.actionCredits.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.actionCredits.setObjectName("actionCredits")
        self.actionSending = QtWidgets.QAction(Main)
        self.actionSending.setCheckable(True)
        self.actionSending.setChecked(True)
        self.actionSending.setObjectName("actionSending")
        self.actionBindings = QtWidgets.QAction(Main)
        self.actionBindings.setCheckable(True)
        self.actionBindings.setChecked(True)
        self.actionBindings.setObjectName("actionBindings")
        self.actionNewBus = QtWidgets.QAction(Main)
        self.actionNewBus.setObjectName("actionNewBus")
        self.actionRecord = QtWidgets.QAction(Main)
        self.actionRecord.setCheckable(True)
        self.actionRecord.setObjectName("actionRecord")
        self.actionReplay = QtWidgets.QAction(Main)
        self.actionReplay.setObjectName("actionReplay")
        self.actionLoad = QtWidgets.QAction(Main)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(Main)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionQuit)
        self.menuAbout.addAction(self.actionCredits)
        self.menuView.addAction(self.actionSending)
        self.menuView.addAction(self.actionBindings)
        self.menuBus.addAction(self.actionRecord)
        self.menuBus.addAction(self.actionReplay)
        self.menuBus.addAction(self.actionSave)
        self.menuBus.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuBus.menuAction())

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "IvyMon Python"))
        self.label_4.setText(_translate("Main", "messages received"))
        self.autoScroll.setText(_translate("Main", "auto scroll"))
        self.label_5.setText(_translate("Main", "ivy events"))
        self.menuFile.setTitle(_translate("Main", "File"))
        self.menuAbout.setTitle(_translate("Main", "About"))
        self.menuView.setTitle(_translate("Main", "View"))
        self.menuBus.setTitle(_translate("Main", "Bus"))
        self.idDock.setWindowTitle(_translate("Main", "identity, sending and agents"))
        self.label.setText(_translate("Main", "bus:"))
        self.busLabel.setText(_translate("Main", "127.255.255.255:2010"))
        self.label_3.setText(_translate("Main", "name:"))
        self.nameLabel.setText(_translate("Main", "IvyMon"))
        self.sendButton.setText(_translate("Main", "send"))
        self.label_7.setText(_translate("Main", "agents on the bus"))
        self.killButton.setText(_translate("Main", "kill"))
        self.inspectButton.setText(_translate("Main", "inspect"))
        self.bindDock.setWindowTitle(_translate("Main", "active bindings"))
        self.removeButton.setText(_translate("Main", "remove"))
        self.addButton.setText(_translate("Main", "add binding"))
        self.actionQuit.setText(_translate("Main", "Quit"))
        self.actionQuit.setShortcut(_translate("Main", "Ctrl+S"))
        self.actionCredits.setText(_translate("Main", "credits"))
        self.actionSending.setText(_translate("Main", "sending"))
        self.actionBindings.setText(_translate("Main", "bindings"))
        self.actionNewBus.setText(_translate("Main", "Join new bus"))
        self.actionRecord.setText(_translate("Main", "record"))
        self.actionReplay.setText(_translate("Main", "replay"))
        self.actionLoad.setText(_translate("Main", "load replay"))
        self.actionSave.setText(_translate("Main", "save replay"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main = QtWidgets.QMainWindow()
    ui = Ui_Main()
    ui.setupUi(Main)
    Main.show()
    sys.exit(app.exec_())

