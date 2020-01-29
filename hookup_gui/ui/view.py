# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

def QString(x=None):
    return x

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1051, 558)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"	background-color: \"#424242\";\n"
"	color: \"white\"\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	background-color: \"#212121\"\n"
"}\n"
"\n"
"QListView {\n"
"	background-color: \"#212121\"\n"
"}\n"
"\n"
"QLabel#label_3, QTextBrowser {\n"
"	background-color: \"#212121\"\n"
"}\n"
"QTextBrowser {\n"
"	border: 1px solid white\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(19)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_ngrok_url = QLabel(self.centralwidget)
        self.label_ngrok_url.setObjectName(u"label_ngrok_url")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_ngrok_url.sizePolicy().hasHeightForWidth())
        self.label_ngrok_url.setSizePolicy(sizePolicy2)
        self.label_ngrok_url.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_ngrok_url)

        self.line_edit_ngrok_url = QLineEdit(self.centralwidget)
        self.line_edit_ngrok_url.setObjectName(u"line_edit_ngrok_url")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line_edit_ngrok_url.sizePolicy().hasHeightForWidth())
        self.line_edit_ngrok_url.setSizePolicy(sizePolicy3)
        self.line_edit_ngrok_url.setMinimumSize(QSize(200, 0))
        self.line_edit_ngrok_url.setStyleSheet(u"border: 1px solid \"#424242\"")
        self.line_edit_ngrok_url.setEchoMode(QLineEdit.Normal)

        self.horizontalLayout.addWidget(self.line_edit_ngrok_url)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tab_configure = QWidget()
        self.tab_configure.setObjectName(u"tab_configure")
        self.tab_configure.setEnabled(True)
        self.tab_configure.setMinimumSize(QSize(0, 304))
        self.verticalLayout_2 = QVBoxLayout(self.tab_configure)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.list_view_pages = QListWidget(self.tab_configure)
        self.list_view_pages.setObjectName(u"list_view_pages")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.list_view_pages.sizePolicy().hasHeightForWidth())
        self.list_view_pages.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.list_view_pages)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, -1, -1)
        self.card = QVBoxLayout()
        self.card.setObjectName(u"card")
        self.label_current_page_name = QLabel(self.tab_configure)
        self.label_current_page_name.setObjectName(u"label_current_page_name")
        self.label_current_page_name.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(15)
        self.label_current_page_name.setFont(font1)
        self.label_current_page_name.setAlignment(Qt.AlignCenter)
        self.label_current_page_name.setMargin(10)

        self.card.addWidget(self.label_current_page_name)

        self.text_browser_current_page_soruce = QTextBrowser(self.tab_configure)
        self.text_browser_current_page_soruce.setObjectName(u"text_browser_current_page_soruce")

        self.card.addWidget(self.text_browser_current_page_soruce)


        self.verticalLayout_3.addLayout(self.card)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_configure, QString())
        self.tab_results = QWidget()
        self.tab_results.setObjectName(u"tab_results")
        self.verticalLayout_4 = QVBoxLayout(self.tab_results)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.refresh_icon = QPushButton(self.tab_results)
        self.refresh_icon.setObjectName(u"refresh_icon")
        self.refresh_icon.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.refresh_icon.sizePolicy().hasHeightForWidth())
        self.refresh_icon.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.refresh_icon)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.list_widget_results = QListWidget(self.tab_results)
        self.list_widget_results.setObjectName(u"list_widget_results")
        self.list_widget_results.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.list_widget_results)

        self.tabWidget.addTab(self.tab_results, QString())

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.list_view_pages, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.text_browser_current_page_soruce)
        QWidget.setTabOrder(self.text_browser_current_page_soruce, self.line_edit_ngrok_url)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HookUp", None))
        self.label_ngrok_url.setText(QCoreApplication.translate("MainWindow", u"Ngrok Url: ", None))
        self.label_current_page_name.setText(QCoreApplication.translate("MainWindow", u"Current Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_configure), QCoreApplication.translate("MainWindow", u"Configure", None))
        self.refresh_icon.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_results), QCoreApplication.translate("MainWindow", u"Results", None))
    # retranslateUi

