# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Windows.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 705)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon_32x32.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(-1)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 2, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 5, 1, 1)
        self.urlbutton = QtWidgets.QPushButton(self.centralwidget)
        self.urlbutton.setMinimumSize(QtCore.QSize(60, 0))
        self.urlbutton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.urlbutton.setObjectName("urlbutton")
        self.gridLayout.addWidget(self.urlbutton, 0, 5, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(60, 0))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 2, 4, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 3, 0, 1, 6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.urlLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.gridLayout.addWidget(self.urlLineEdit, 0, 0, 1, 5)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 4)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 5, 4, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(60, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(60, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 5, 3, 1, 1)
        self.saveConf = QtWidgets.QPushButton(self.centralwidget)
        self.saveConf.setMinimumSize(QtCore.QSize(60, 0))
        self.saveConf.setMaximumSize(QtCore.QSize(80, 16777215))
        self.saveConf.setObjectName("saveConf")
        self.gridLayout.addWidget(self.saveConf, 7, 5, 1, 1)
        self.nextPage = QtWidgets.QPushButton(self.centralwidget)
        self.nextPage.setMinimumSize(QtCore.QSize(60, 0))
        self.nextPage.setMaximumSize(QtCore.QSize(80, 16777215))
        self.nextPage.setObjectName("nextPage")
        self.gridLayout.addWidget(self.nextPage, 5, 5, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMinimumSize(QtCore.QSize(1, 0))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setShowGrid(False)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_4 = QtWidgets.QMenu(self.menu)
        self.menu_4.setObjectName("menu_4")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.actionjiankong = QtWidgets.QAction(MainWindow)
        self.actionjiankong.setObjectName("actionjiankong")
        self.actionLiebiao = QtWidgets.QAction(MainWindow)
        self.actionLiebiao.setObjectName("actionLiebiao")
        self.actionNeirong = QtWidgets.QAction(MainWindow)
        self.actionNeirong.setObjectName("actionNeirong")
        self.menu_4.addAction(self.actionLiebiao)
        self.menu_4.addAction(self.actionNeirong)
        self.menu.addAction(self.menu_4.menuAction())
        self.menu.addAction(self.actionjiankong)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "爬虫管理"))
        self.label.setText(_translate("MainWindow", "列表区域"))
        self.pushButton_3.setText(_translate("MainWindow", "添加"))
        self.pushButton.setText(_translate("MainWindow", "测试"))
        self.urlbutton.setText(_translate("MainWindow", "获取源码"))
        self.lineEdit_2.setText(_translate("MainWindow", "标题名"))
        self.pushButton_2.setText(_translate("MainWindow", "测试"))
        self.label_2.setText(_translate("MainWindow", "下一页"))
        self.urlLineEdit.setText(_translate("MainWindow", "请输入列表页面的网址"))
        self.lineEdit.setText(_translate("MainWindow", "请输入正确范围的xpath"))
        self.pushButton_4.setText(_translate("MainWindow", "测试"))
        self.comboBox.setItemText(0, _translate("MainWindow", "文本"))
        self.comboBox.setItemText(1, _translate("MainWindow", "连接"))
        self.comboBox.setItemText(2, _translate("MainWindow", "数组"))
        self.comboBox.setItemText(3, _translate("MainWindow", "数组转文本"))
        self.comboBox.setItemText(4, _translate("MainWindow", "文本拼接"))
        self.comboBox.setItemText(5, _translate("MainWindow", "文本截取"))
        self.comboBox.setItemText(6, _translate("MainWindow", "数组截取"))
        self.comboBox.setItemText(7, _translate("MainWindow", "二值转换"))
        self.comboBox.setItemText(8, _translate("MainWindow", "二值逆转换"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "文本"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "连接"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "数组"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "数组转文本"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "文本拼接"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "文本截取"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "数组截取"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "二值转换"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "二值逆转换"))
        self.saveConf.setText(_translate("MainWindow", "保存配置"))
        self.nextPage.setText(_translate("MainWindow", "翻页"))
        self.lineEdit_3.setText(_translate("MainWindow", "xpath"))
        self.menu.setTitle(_translate("MainWindow", "创建"))
        self.menu_4.setTitle(_translate("MainWindow", "新建任务"))
        self.menu_2.setTitle(_translate("MainWindow", "关于我们"))
        self.menu_3.setTitle(_translate("MainWindow", "分析"))
        self.actionjiankong.setText(_translate("MainWindow", "监控"))
        self.actionLiebiao.setText(_translate("MainWindow", "列表"))
        self.actionNeirong.setText(_translate("MainWindow", "内容"))

