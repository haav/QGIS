# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_pointadjust.ui'
#
# Created: Thu Jan 24 00:45:33 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PointAdjust(object):
    def setupUi(self, PointAdjust):
        PointAdjust.setObjectName(_fromUtf8("PointAdjust"))
        PointAdjust.resize(410, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PointAdjust.sizePolicy().hasHeightForWidth())
        PointAdjust.setSizePolicy(sizePolicy)
        PointAdjust.setMinimumSize(QtCore.QSize(410, 300))
        PointAdjust.setMaximumSize(QtCore.QSize(410, 300))
        self.tabWidget = QtGui.QTabWidget(PointAdjust)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 391, 281))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lblLayer = QtGui.QLabel(self.tab)
        self.lblLayer.setGeometry(QtCore.QRect(20, 10, 101, 16))
        self.lblLayer.setObjectName(_fromUtf8("lblLayer"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 361, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.fid2 = QtGui.QLineEdit(self.groupBox)
        self.fid2.setGeometry(QtCore.QRect(70, 90, 41, 20))
        self.fid2.setObjectName(_fromUtf8("fid2"))
        self.x2 = QtGui.QLineEdit(self.groupBox)
        self.x2.setGeometry(QtCore.QRect(140, 90, 91, 20))
        self.x2.setObjectName(_fromUtf8("x2"))
        self.x1 = QtGui.QLineEdit(self.groupBox)
        self.x1.setGeometry(QtCore.QRect(140, 40, 91, 20))
        self.x1.setObjectName(_fromUtf8("x1"))
        self.y1 = QtGui.QLineEdit(self.groupBox)
        self.y1.setGeometry(QtCore.QRect(260, 40, 91, 20))
        self.y1.setObjectName(_fromUtf8("y1"))
        self.fid1 = QtGui.QLineEdit(self.groupBox)
        self.fid1.setGeometry(QtCore.QRect(70, 40, 41, 20))
        self.fid1.setObjectName(_fromUtf8("fid1"))
        self.y2 = QtGui.QLineEdit(self.groupBox)
        self.y2.setGeometry(QtCore.QRect(260, 90, 91, 20))
        self.y2.setObjectName(_fromUtf8("y2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 40, 16, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(240, 40, 16, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(120, 90, 16, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(240, 90, 16, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 46, 13))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 331, 31))
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboLayer = QtGui.QComboBox(self.tab)
        self.comboLayer.setGeometry(QtCore.QRect(120, 10, 251, 22))
        self.comboLayer.setObjectName(_fromUtf8("comboLayer"))
        self.buttonBox = QtGui.QDialogButtonBox(self.tab)
        self.buttonBox.setGeometry(QtCore.QRect(210, 220, 151, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 371, 241))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(PointAdjust)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), PointAdjust.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), PointAdjust.reject)
        QtCore.QMetaObject.connectSlotsByName(PointAdjust)
        PointAdjust.setTabOrder(self.tabWidget, self.comboLayer)
        PointAdjust.setTabOrder(self.comboLayer, self.fid1)
        PointAdjust.setTabOrder(self.fid1, self.x1)
        PointAdjust.setTabOrder(self.x1, self.y1)
        PointAdjust.setTabOrder(self.y1, self.fid2)
        PointAdjust.setTabOrder(self.fid2, self.x2)
        PointAdjust.setTabOrder(self.x2, self.y2)
        PointAdjust.setTabOrder(self.y2, self.buttonBox)

    def retranslateUi(self, PointAdjust):
        PointAdjust.setWindowTitle(QtGui.QApplication.translate("PointAdjust", "Point adjustment", None, QtGui.QApplication.UnicodeUTF8))
        self.lblLayer.setText(QtGui.QApplication.translate("PointAdjust", "Vector point layer:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("PointAdjust", "Adjustment parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PointAdjust", "Point A", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("PointAdjust", "Feature ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("PointAdjust", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("PointAdjust", "Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("PointAdjust", "Feature ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("PointAdjust", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("PointAdjust", "Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("PointAdjust", "Point B", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("PointAdjust", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-style:italic;\">Example:<br />Feature ID:   3              X:      652142.2342          Y:     58024.7543 </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("PointAdjust", "Point adjustment", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("PointAdjust", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:16pt; font-weight:600;\">Point Adjustment</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:600;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">(c) Copyright 2013 Allar Haav</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">licensed under the terms of GNU GPL v3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:9pt;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">This is a tool for making spatial adjustment, namely similarity transformation, to a point vector layer. It does, however, not alter the scale and therefore performs only the translation and rotation operations maintaining the original dimensions. Useful for total station point data in arbitrary coordinate system when there are a few points with known &quot;real-life&quot; coordinates.<br /><br />The plugin functions as follows:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">* A vector point layer is selected with edit mode enabled</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">* Point A is chosen and its feature ID entered. The coordinates entered in the X and Y fields will specify the new location of the point. It is important to keep in mind that point A will be used as the pivot point for rotation.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">* The corresponding fields are filled for point B. This point will be used to obtain the correct angle for rotation. The deviation from the expected location for point B will be indicated in a dialog box, but will only affect the rotation for the layer, not its shape nor location.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:9pt;\"></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'DejaVu Sans\'; font-size:9pt;\"></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'DejaVu Sans\'; font-size:9pt;\">If you have any comments or suggestions, feel free to mail me: allar.haav@gmail.com</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("PointAdjust", "Help", None, QtGui.QApplication.UnicodeUTF8))

