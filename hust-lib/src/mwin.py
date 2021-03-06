# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MWin(object):
    def setupUi(self, MWin):
        MWin.setObjectName("MWin")
        MWin.resize(720, 405)
        MWin.setMinimumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        MWin.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/library.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MWin.setWindowIcon(icon)
        MWin.setIconSize(QtCore.QSize(30, 30))
        self.centralWidget = QtWidgets.QWidget(MWin)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab1 = QtWidgets.QWidget()
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.keyword = QtWidgets.QLineEdit(self.tab1)
        self.keyword.setMinimumSize(QtCore.QSize(0, 28))
        self.keyword.setObjectName("keyword")
        self.horizontalLayout.addWidget(self.keyword)
        self.search_btn = QtWidgets.QToolButton(self.tab1)
        self.search_btn.setMinimumSize(QtCore.QSize(60, 30))
        self.search_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableWidget(self.tab1)
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.table)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pre_page_btn = QtWidgets.QToolButton(self.tab1)
        self.pre_page_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.pre_page_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pre_page_btn.setObjectName("pre_page_btn")
        self.horizontalLayout_3.addWidget(self.pre_page_btn)
        self.current_page_index = QtWidgets.QLabel(self.tab1)
        self.current_page_index.setObjectName("current_page_index")
        self.horizontalLayout_3.addWidget(self.current_page_index)
        self.page_count = QtWidgets.QLabel(self.tab1)
        self.page_count.setObjectName("page_count")
        self.horizontalLayout_3.addWidget(self.page_count)
        self.jump_page = QtWidgets.QSpinBox(self.tab1)
        self.jump_page.setMinimum(1)
        self.jump_page.setObjectName("jump_page")
        self.horizontalLayout_3.addWidget(self.jump_page)
        self.jump_page_btn = QtWidgets.QToolButton(self.tab1)
        self.jump_page_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.jump_page_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.jump_page_btn.setObjectName("jump_page_btn")
        self.horizontalLayout_3.addWidget(self.jump_page_btn)
        self.next_page_btn = QtWidgets.QToolButton(self.tab1)
        self.next_page_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.next_page_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_page_btn.setObjectName("next_page_btn")
        self.horizontalLayout_3.addWidget(self.next_page_btn)
        self.last_page_btn = QtWidgets.QToolButton(self.tab1)
        self.last_page_btn.setMinimumSize(QtCore.QSize(80, 0))
        self.last_page_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.last_page_btn.setObjectName("last_page_btn")
        self.horizontalLayout_3.addWidget(self.last_page_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab2)
        self.verticalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.tab2)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.tab2)
        self.label_4.setStyleSheet("color:#bbb")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.tabWidget.addTab(self.tab2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MWin.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MWin)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 720, 23))
        self.menuBar.setObjectName("menuBar")
        MWin.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MWin)
        self.statusBar.setObjectName("statusBar")
        MWin.setStatusBar(self.statusBar)

        self.retranslateUi(MWin)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MWin)

    def retranslateUi(self, MWin):
        _translate = QtCore.QCoreApplication.translate
        MWin.setWindowTitle(_translate("MWin", "华中科技大学图书馆公共查询系统"))
        self.keyword.setPlaceholderText(_translate("MWin", "在此输入查询的关键词..."))
        self.search_btn.setText(_translate("MWin", "查 询"))
        self.search_btn.setShortcut(_translate("MWin", "Return"))
        self.pre_page_btn.setText(_translate("MWin", "前一页"))
        self.pre_page_btn.setShortcut(_translate("MWin", "Ctrl+B"))
        self.current_page_index.setText(_translate("MWin", "当前 1 页"))
        self.page_count.setText(_translate("MWin", "一共 1 页"))
        self.jump_page_btn.setText(_translate("MWin", "跳转"))
        self.jump_page_btn.setShortcut(_translate("MWin", "Ctrl+Return"))
        self.next_page_btn.setText(_translate("MWin", "后一页"))
        self.next_page_btn.setShortcut(_translate("MWin", "Ctrl+N"))
        self.last_page_btn.setText(_translate("MWin", "最后一页"))
        self.last_page_btn.setShortcut(_translate("MWin", "Ctrl+Shift+N"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), _translate("MWin", "首页"))
        self.groupBox_2.setTitle(_translate("MWin", "关于本软件"))
        self.label_3.setText(_translate("MWin", "本软件仅将网页在线查询功能放到一个程序中（以爬虫的形式获取对应的链接/资源）\n"
"v0.0.1 第一个简单版本@2019/2/20"))
        self.groupBox.setTitle(_translate("MWin", "bug反馈"))
        self.label.setText(_translate("MWin", "GitHub：<a href=\'https://github.com/LewisTian/PyQt5-Apps\'>https://github.com/LewisTian/PyQt5-Apps</a>"))
        self.label_2.setText(_translate("MWin", "Email：lewissmith@126.com"))
        self.label_4.setText(_translate("MWin", "— 我是有底线的 —"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), _translate("MWin", "关于"))

import res_rc
