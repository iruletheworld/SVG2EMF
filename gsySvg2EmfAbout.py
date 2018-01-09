# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(525, 325)
        About.setMinimumSize(QtCore.QSize(525, 325))
        About.setMaximumSize(QtCore.QSize(525, 350))
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_text = QtWidgets.QLabel(self.centralwidget)
        self.lbl_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_text.setWordWrap(True)
        self.lbl_text.setObjectName("lbl_text")
        self.gridLayout.addWidget(self.lbl_text, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(373, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout.addWidget(self.btn_close, 1, 1, 1, 1)
        About.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(About)
        self.statusbar.setObjectName("statusbar")
        About.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(About)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(About)
        self.btn_close.clicked.connect(About.close)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About Symmetrical Components"))
        self.lbl_text.setText(_translate("About", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">About SVG2EMF </span><br/></p><p>Version 0.1.0.</p><p>SVG2EMF is a program designed to be a wrapper program for Inkscape to convert SVG files to EMF files. To use this program, you must install <a href=\"https://inkscape.org\">Inkscape</a> first.</p><p>This program is licensed under Apache 2.0. </p><p>Details of this program can be found in the documentation.</p><p>This program is designed for Windows.</p><p>This program is developed by 高斯羽 博士(Dr. GAO, Siyu).</p></body></html>"))
        self.lbl_text.setOpenExternalLinks(True)
        self.btn_close.setText(_translate("About", "Close"))
        self.actionExit.setText(_translate("About", "exit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QMainWindow()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

