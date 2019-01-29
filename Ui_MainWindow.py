# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listArea = QtWidgets.QScrollArea(self.centralwidget)
        self.listArea.setMinimumSize(QtCore.QSize(200, 0))
        self.listArea.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listArea.setWidgetResizable(True)
        self.listArea.setObjectName("listArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 198, 499))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.listArea)
        self.showArea = QtWidgets.QScrollArea(self.centralwidget)
        self.showArea.setWidgetResizable(True)
        self.showArea.setObjectName("showArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 572, 499))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.showArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout.addWidget(self.showArea)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 32))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/res/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/res/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon1)
        self.actionSave.setObjectName("actionSave")
        self.actionSaveAs = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/res/picturetopgallery.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveAs.setIcon(icon2)
        self.actionSaveAs.setObjectName("actionSaveAs")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/res/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon3)
        self.actionPrint.setObjectName("actionPrint")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/res/res/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon4)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/res/res/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon5)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAppend = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/res/res/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAppend.setIcon(icon6)
        self.actionAppend.setObjectName("actionAppend")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/res/res/del.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon7)
        self.actionDelete.setObjectName("actionDelete")
        self.actionExtract = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/res/res/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExtract.setIcon(icon8)
        self.actionExtract.setObjectName("actionExtract")
        self.actionMove = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/res/res/sort.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMove.setIcon(icon9)
        self.actionMove.setObjectName("actionMove")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/res/res/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon10)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/res/res/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon11)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/res/res/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon12)
        self.actionCopy.setObjectName("actionCopy")
        self.actionRotate = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/res/res/convert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRotate.setIcon(icon13)
        self.actionRotate.setObjectName("actionRotate")
        self.actionPicToPdf = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/res/res/address.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPicToPdf.setIcon(icon14)
        self.actionPicToPdf.setObjectName("actionPicToPdf")
        self.actionMerge = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/res/res/custom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMerge.setIcon(icon15)
        self.actionMerge.setObjectName("actionMerge")
        self.menu.addAction(self.actionOpen)
        self.menu.addSeparator()
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionSaveAs)
        self.menu.addSeparator()
        self.menu.addAction(self.actionPrint)
        self.menu.addSeparator()
        self.menu.addAction(self.actionClose)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menu_2.addAction(self.actionAppend)
        self.menu_2.addAction(self.actionExtract)
        self.menu_2.addAction(self.actionCopy)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionMove)
        self.menu_2.addAction(self.actionRotate)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionDelete)
        self.menu_3.addAction(self.actionHelp)
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionAbout)
        self.menu_4.addAction(self.actionPicToPdf)
        self.menu_4.addAction(self.actionMerge)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addAction(self.actionPrint)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAppend)
        self.toolBar.addAction(self.actionExtract)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionMove)
        self.toolBar.addAction(self.actionRotate)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPicToPdf)
        self.toolBar.addAction(self.actionMerge)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pdfEdit"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "操作"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.menu_4.setTitle(_translate("MainWindow", "转换"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "打开..."))
        self.actionSave.setText(_translate("MainWindow", "保存"))
        self.actionSaveAs.setText(_translate("MainWindow", "另存为..."))
        self.actionPrint.setText(_translate("MainWindow", "打印"))
        self.actionClose.setText(_translate("MainWindow", "关闭"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionAppend.setText(_translate("MainWindow", "追加"))
        self.actionDelete.setText(_translate("MainWindow", "删除"))
        self.actionExtract.setText(_translate("MainWindow", "导出"))
        self.actionMove.setText(_translate("MainWindow", "移动"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About ..."))
        self.actionCopy.setText(_translate("MainWindow", "拷贝"))
        self.actionRotate.setText(_translate("MainWindow", "旋转"))
        self.actionPicToPdf.setText(_translate("MainWindow", "图片转PDF"))
        self.actionMerge.setText(_translate("MainWindow", "合并PDF"))

import PdfRes_rc
