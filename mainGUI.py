# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 612)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gLayMain = QtWidgets.QGridLayout()
        self.gLayMain.setObjectName("gLayMain")
        self.tblOutput = QtWidgets.QTableWidget(self.centralwidget)
        self.tblOutput.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tblOutput.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblOutput.setDragEnabled(False)
        self.tblOutput.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tblOutput.setWordWrap(True)
        self.tblOutput.setObjectName("tblOutput")
        self.tblOutput.setColumnCount(2)
        self.tblOutput.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblOutput.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblOutput.setHorizontalHeaderItem(1, item)
        self.tblOutput.horizontalHeader().setStretchLastSection(True)
        self.gLayMain.addWidget(self.tblOutput, 1, 1, 1, 1)
        self.hLayThresholds = QtWidgets.QHBoxLayout()
        self.hLayThresholds.setObjectName("hLayThresholds")
        self.lblTimeThresh = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTimeThresh.sizePolicy().hasHeightForWidth())
        self.lblTimeThresh.setSizePolicy(sizePolicy)
        self.lblTimeThresh.setObjectName("lblTimeThresh")
        self.hLayThresholds.addWidget(self.lblTimeThresh)
        self.txtTimeThr = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtTimeThr.sizePolicy().hasHeightForWidth())
        self.txtTimeThr.setSizePolicy(sizePolicy)
        self.txtTimeThr.setObjectName("txtTimeThr")
        self.hLayThresholds.addWidget(self.txtTimeThr)
        self.lblChargeThresh = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblChargeThresh.sizePolicy().hasHeightForWidth())
        self.lblChargeThresh.setSizePolicy(sizePolicy)
        self.lblChargeThresh.setObjectName("lblChargeThresh")
        self.hLayThresholds.addWidget(self.lblChargeThresh)
        self.txtChargeThr = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtChargeThr.sizePolicy().hasHeightForWidth())
        self.txtChargeThr.setSizePolicy(sizePolicy)
        self.txtChargeThr.setObjectName("txtChargeThr")
        self.hLayThresholds.addWidget(self.txtChargeThr)
        self.gLayMain.addLayout(self.hLayThresholds, 0, 0, 1, 1)
        self.hLayButtons = QtWidgets.QHBoxLayout()
        self.hLayButtons.setObjectName("hLayButtons")
        self.btnGen = QtWidgets.QPushButton(self.centralwidget)
        self.btnGen.setObjectName("btnGen")
        self.hLayButtons.addWidget(self.btnGen)
        self.btnCopy = QtWidgets.QPushButton(self.centralwidget)
        self.btnCopy.setObjectName("btnCopy")
        self.hLayButtons.addWidget(self.btnCopy)
        self.gLayMain.addLayout(self.hLayButtons, 0, 1, 1, 1)
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setObjectName("btnSave")
        self.gLayMain.addWidget(self.btnSave, 2, 1, 1, 1)
        self.tabGroupOrCh = QtWidgets.QTabWidget(self.centralwidget)
        self.tabGroupOrCh.setObjectName("tabGroupOrCh")
        self.tabGroup = QtWidgets.QWidget()
        self.tabGroup.setObjectName("tabGroup")
        self.gridLayout = QtWidgets.QGridLayout(self.tabGroup)
        self.gridLayout.setObjectName("gridLayout")
        self.cmbTR2LG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbTR2LG.sizePolicy().hasHeightForWidth())
        self.cmbTR2LG.setSizePolicy(sizePolicy)
        self.cmbTR2LG.setObjectName("cmbTR2LG")
        self.gridLayout.addWidget(self.cmbTR2LG, 2, 2, 1, 1)
        self.lblLG = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLG.sizePolicy().hasHeightForWidth())
        self.lblLG.setSizePolicy(sizePolicy)
        self.lblLG.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLG.setObjectName("lblLG")
        self.gridLayout.addWidget(self.lblLG, 0, 2, 1, 1)
        self.lblRAN = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRAN.sizePolicy().hasHeightForWidth())
        self.lblRAN.setSizePolicy(sizePolicy)
        self.lblRAN.setAlignment(QtCore.Qt.AlignCenter)
        self.lblRAN.setObjectName("lblRAN")
        self.gridLayout.addWidget(self.lblRAN, 3, 0, 1, 1)
        self.cmbTR1HG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbTR1HG.sizePolicy().hasHeightForWidth())
        self.cmbTR1HG.setSizePolicy(sizePolicy)
        self.cmbTR1HG.setObjectName("cmbTR1HG")
        self.gridLayout.addWidget(self.cmbTR1HG, 1, 1, 1, 1)
        self.lblTR2 = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTR2.sizePolicy().hasHeightForWidth())
        self.lblTR2.setSizePolicy(sizePolicy)
        self.lblTR2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTR2.setObjectName("lblTR2")
        self.gridLayout.addWidget(self.lblTR2, 2, 0, 1, 1)
        self.lblGroups = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblGroups.sizePolicy().hasHeightForWidth())
        self.lblGroups.setSizePolicy(sizePolicy)
        self.lblGroups.setAlignment(QtCore.Qt.AlignCenter)
        self.lblGroups.setObjectName("lblGroups")
        self.gridLayout.addWidget(self.lblGroups, 0, 0, 1, 1)
        self.cmbTR1LG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbTR1LG.sizePolicy().hasHeightForWidth())
        self.cmbTR1LG.setSizePolicy(sizePolicy)
        self.cmbTR1LG.setObjectName("cmbTR1LG")
        self.gridLayout.addWidget(self.cmbTR1LG, 1, 2, 1, 1)
        self.cmbRANHG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbRANHG.sizePolicy().hasHeightForWidth())
        self.cmbRANHG.setSizePolicy(sizePolicy)
        self.cmbRANHG.setObjectName("cmbRANHG")
        self.gridLayout.addWidget(self.cmbRANHG, 3, 1, 1, 1)
        self.lblLYSO = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLYSO.sizePolicy().hasHeightForWidth())
        self.lblLYSO.setSizePolicy(sizePolicy)
        self.lblLYSO.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLYSO.setObjectName("lblLYSO")
        self.gridLayout.addWidget(self.lblLYSO, 4, 0, 1, 1)
        self.cmbTR2HG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbTR2HG.sizePolicy().hasHeightForWidth())
        self.cmbTR2HG.setSizePolicy(sizePolicy)
        self.cmbTR2HG.setObjectName("cmbTR2HG")
        self.gridLayout.addWidget(self.cmbTR2HG, 2, 1, 1, 1)
        self.cmbRANLG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbRANLG.sizePolicy().hasHeightForWidth())
        self.cmbRANLG.setSizePolicy(sizePolicy)
        self.cmbRANLG.setObjectName("cmbRANLG")
        self.gridLayout.addWidget(self.cmbRANLG, 3, 2, 1, 1)
        self.cmbLYSOLG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLYSOLG.sizePolicy().hasHeightForWidth())
        self.cmbLYSOLG.setSizePolicy(sizePolicy)
        self.cmbLYSOLG.setObjectName("cmbLYSOLG")
        self.gridLayout.addWidget(self.cmbLYSOLG, 4, 2, 1, 1)
        self.lblTR1 = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTR1.sizePolicy().hasHeightForWidth())
        self.lblTR1.setSizePolicy(sizePolicy)
        self.lblTR1.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTR1.setObjectName("lblTR1")
        self.gridLayout.addWidget(self.lblTR1, 1, 0, 1, 1)
        self.cmbLYSOHG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLYSOHG.sizePolicy().hasHeightForWidth())
        self.cmbLYSOHG.setSizePolicy(sizePolicy)
        self.cmbLYSOHG.setObjectName("cmbLYSOHG")
        self.gridLayout.addWidget(self.cmbLYSOHG, 4, 1, 1, 1)
        self.lblHG = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHG.sizePolicy().hasHeightForWidth())
        self.lblHG.setSizePolicy(sizePolicy)
        self.lblHG.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHG.setObjectName("lblHG")
        self.gridLayout.addWidget(self.lblHG, 0, 1, 1, 1)
        self.lblLATBOT = QtWidgets.QLabel(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblLATBOT.sizePolicy().hasHeightForWidth())
        self.lblLATBOT.setSizePolicy(sizePolicy)
        self.lblLATBOT.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLATBOT.setObjectName("lblLATBOT")
        self.gridLayout.addWidget(self.lblLATBOT, 5, 0, 1, 1)
        self.cmbLATBOTHG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLATBOTHG.sizePolicy().hasHeightForWidth())
        self.cmbLATBOTHG.setSizePolicy(sizePolicy)
        self.cmbLATBOTHG.setObjectName("cmbLATBOTHG")
        self.gridLayout.addWidget(self.cmbLATBOTHG, 5, 1, 1, 1)
        self.cmbLATBOTLG = QtWidgets.QComboBox(self.tabGroup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbLATBOTLG.sizePolicy().hasHeightForWidth())
        self.cmbLATBOTLG.setSizePolicy(sizePolicy)
        self.cmbLATBOTLG.setObjectName("cmbLATBOTLG")
        self.gridLayout.addWidget(self.cmbLATBOTLG, 5, 2, 1, 1)
        self.gridLayout.setColumnStretch(0, 60)
        self.gridLayout.setColumnStretch(1, 10)
        self.gridLayout.setColumnStretch(2, 10)
        self.gridLayout.setRowStretch(0, 10)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 20)
        self.gridLayout.setRowStretch(3, 20)
        self.gridLayout.setRowStretch(4, 20)
        self.gridLayout.setRowStretch(5, 20)
        self.tabGroupOrCh.addTab(self.tabGroup, "")
        self.tabChannels = QtWidgets.QWidget()
        self.tabChannels.setObjectName("tabChannels")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tabChannels)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.tabChannels)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrlAreaCnt = QtWidgets.QWidget()
        self.scrlAreaCnt.setGeometry(QtCore.QRect(0, 0, 414, 515))
        self.scrlAreaCnt.setObjectName("scrlAreaCnt")
        self.vLayScroll = QtWidgets.QVBoxLayout(self.scrlAreaCnt)
        self.vLayScroll.setObjectName("vLayScroll")
        self.scrollArea.setWidget(self.scrlAreaCnt)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.tabGroupOrCh.addTab(self.tabChannels, "")
        self.gLayMain.addWidget(self.tabGroupOrCh, 1, 0, 2, 1)
        self.verticalLayout.addLayout(self.gLayMain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionCopy_as_dictionary = QtWidgets.QAction(MainWindow)
        self.actionCopy_as_dictionary.setCheckable(True)
        self.actionCopy_as_dictionary.setObjectName("actionCopy_as_dictionary")
        self.actionCopy_as_python_dictionary = QtWidgets.QAction(MainWindow)
        self.actionCopy_as_python_dictionary.setCheckable(True)
        self.actionCopy_as_python_dictionary.setObjectName("actionCopy_as_python_dictionary")
        self.actCopyAsCmd = QtWidgets.QAction(MainWindow)
        self.actCopyAsCmd.setCheckable(True)
        self.actCopyAsCmd.setObjectName("actCopyAsCmd")
        self.actCopyAsDict = QtWidgets.QAction(MainWindow)
        self.actCopyAsDict.setCheckable(True)
        self.actCopyAsDict.setObjectName("actCopyAsDict")

        self.retranslateUi(MainWindow)
        self.tabGroupOrCh.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CITIROC Configurator for HEPD-02"))
        item = self.tblOutput.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tblOutput.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.lblTimeThresh.setText(_translate("MainWindow", "Time Threshold"))
        self.txtTimeThr.setInputMask(_translate("MainWindow", "9000"))
        self.txtTimeThr.setText(_translate("MainWindow", "230"))
        self.lblChargeThresh.setText(_translate("MainWindow", "Charge Threshold"))
        self.txtChargeThr.setInputMask(_translate("MainWindow", "9000"))
        self.txtChargeThr.setText(_translate("MainWindow", "230"))
        self.btnGen.setText(_translate("MainWindow", "Generate configuration"))
        self.btnCopy.setText(_translate("MainWindow", "Copy to clipboard"))
        self.btnSave.setText(_translate("MainWindow", "Save to file"))
        self.lblLG.setText(_translate("MainWindow", "LG"))
        self.lblRAN.setText(_translate("MainWindow", "RAN"))
        self.lblTR2.setText(_translate("MainWindow", "TR2"))
        self.lblGroups.setText(_translate("MainWindow", "HEPD-02 channel group"))
        self.lblLYSO.setText(_translate("MainWindow", "LYSO"))
        self.lblTR1.setText(_translate("MainWindow", "TR1"))
        self.lblHG.setText(_translate("MainWindow", "HG"))
        self.lblLATBOT.setText(_translate("MainWindow", "LAT and BOT"))
        self.tabGroupOrCh.setTabText(self.tabGroupOrCh.indexOf(self.tabGroup), _translate("MainWindow", "HEPD-02 groups"))
        self.tabGroupOrCh.setTabText(self.tabGroupOrCh.indexOf(self.tabChannels), _translate("MainWindow", "CITIROC channels"))
        self.actionCopy_as_dictionary.setText(_translate("MainWindow", "Copy as command string"))
        self.actionCopy_as_python_dictionary.setText(_translate("MainWindow", "Copy as python dictionary"))
        self.actCopyAsCmd.setText(_translate("MainWindow", "Copy as egse command string"))
        self.actCopyAsDict.setText(_translate("MainWindow", "Copy as python dictionary"))
