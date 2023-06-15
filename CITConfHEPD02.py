#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem,
                             QLabel, QHBoxLayout, QComboBox,
                             QCheckBox, QFileDialog, QMessageBox)
from mainGUI import Ui_MainWindow
from citSupportLib import HGValidGains, LGValidGains, InCALIBValidGains
from getCITConfig import getConf, defGains
import re

channelPattern = "Ch(\d\d?)"
chRegex = re.compile(channelPattern)

plastDefGainHG = 20.0
plastDefGainLG = 2.0
lysoDefGainHG = 10.0
lysoDefGainLG = 1.5
inCalibDefGain = 4.0

class mainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, clipBoard):
        super().__init__()
        self.gains = defGains
        self.clipboard = clipBoard
        self.cConf = None
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.initGroupTab()

        for i in range(17):
            item = "0x"+f"{i+9:08x}".upper()
            self.tblOutput.insertRow(i)
            self.tblOutput.setItem(i , 0, QTableWidgetItem(item))

        self.initSingleChTab()

        self.btnGen.clicked.connect(self.genConf)
        self.btnCopy.clicked.connect(self.copyToClipboard)
        self.btnSave.clicked.connect(self.saveToFile)

    def initComboBox(self, cmb, validGains, defGain):
        cmb.clear()
        cmb.addItems([str(v) for v in validGains])
        cmb.setCurrentIndex(validGains.index(defGain))

    def initGroupTab(self):
        self.initComboBox(self.cmbTR1HG,    HGValidGains, plastDefGainHG)
        self.initComboBox(self.cmbTR1LG,    LGValidGains, plastDefGainLG)
        self.initComboBox(self.cmbTR2HG,    HGValidGains, plastDefGainHG)
        self.initComboBox(self.cmbTR2LG,    LGValidGains, plastDefGainLG)
        self.initComboBox(self.cmbRANHG,    HGValidGains, plastDefGainHG)
        self.initComboBox(self.cmbRANLG,    LGValidGains, plastDefGainLG)
        self.initComboBox(self.cmbLYSOHG,   HGValidGains, lysoDefGainHG)
        self.initComboBox(self.cmbLYSOLG,   LGValidGains, lysoDefGainLG)
        self.initComboBox(self.cmbLATBOTHG, HGValidGains, plastDefGainHG)
        self.initComboBox(self.cmbLATBOTLG, LGValidGains, plastDefGainLG)

    def initSingleChTab(self):
        self.hLaySingleCh = []
        self.sChLabels    = []
        self.sChCmbHG     = []
        self.sChCmbLG     = []
        self.sChInCalib   = []
        self.sChDisabled  = []
        for i in range(32):
            initValHG = plastDefGainHG if (i < 21 or i > 26) else lysoDefGainHG
            initValLG = plastDefGainLG if (i < 21 or i > 26) else lysoDefGainLG

            hLaySCh = QHBoxLayout()
            hLaySCh.setObjectName(f"hLaySingleCh{i}")

            lblCh = QLabel()
            lblCh.setObjectName(f"lblCh{i}")
            lblCh.setText(f"Channel {i:02d}")
            
            cmbHG = QComboBox()
            cmbHG.setObjectName(f"cmbHGCh{i}")
            self.initComboBox(cmbHG, HGValidGains, initValHG)

            cmbLG = QComboBox()
            cmbLG.setObjectName(f"cmbLGCh{i}")
            self.initComboBox(cmbLG, LGValidGains, initValLG)            

            cmbInCalib = QComboBox()
            cmbInCalib.setObjectName(f"cmbInCalibCh{i}")
            cmbInCalib.addItems(["None","HG","LG"])
            cmbInCalib.currentIndexChanged.connect(self.cmbInCalibGains)

            chkDisabled = QCheckBox()
            chkDisabled.setObjectName(f"chkDisabledCh{i}")
            chkDisabled.setText("Disable")

            self.sChLabels.append(lblCh)
            self.sChCmbHG.append(cmbHG)
            self.sChCmbLG.append(cmbLG)
            self.sChInCalib.append(cmbInCalib)
            self.sChDisabled.append(chkDisabled)
            
            hLaySCh.addWidget(lblCh)
            hLaySCh.addWidget(cmbHG)
            hLaySCh.addWidget(cmbLG)
            hLaySCh.addWidget(cmbInCalib)
            hLaySCh.addWidget(chkDisabled)
            
            self.hLaySingleCh.append(hLaySCh)

            self.vLayScroll.addLayout(hLaySCh)

    def cmbInCalibGains(self):
        sender = self.sender()
        selectedGain = sender.currentText()
        cmbName = sender.objectName()
        channel = chRegex.findall(cmbName)

        if channel == []:
            return
        
        ch = int(channel[0])

        cmbHG = self.findChild(QComboBox, f"cmbHGCh{ch}")
        cmbLG = self.findChild(QComboBox, f"cmbLGCh{ch}")

        defHG = plastDefGainHG if (ch < 21 or ch > 26) else lysoDefGainHG
        defLG = plastDefGainLG if (ch < 21 or ch > 26) else lysoDefGainLG

        if selectedGain == "HG":
            hgGainSel = InCALIBValidGains
            lgGainSel = LGValidGains
            initValHG = inCalibDefGain
            initValLG = defLG

        elif selectedGain == "LG":
            hgGainSel = HGValidGains
            lgGainSel = InCALIBValidGains
            initValHG = defHG
            initValLG = inCalibDefGain

        else:
            hgGainSel = HGValidGains
            lgGainSel = LGValidGains
            initValHG = defHG
            initValLG = defLG

        self.initComboBox(cmbHG, hgGainSel, initValHG)
        self.initComboBox(cmbLG, lgGainSel, initValLG)

    def genConf(self):
        selectedTab = self.tabGroupOrCh.currentIndex()
        timeThr = int(self.txtTimeThr.text())
        chargeThr = int(self.txtChargeThr.text())

        if selectedTab == 0:
            self.genConfGroup(timeThr, chargeThr)
        else:
            self.genConfChannels(timeThr, chargeThr)

        self.cConf = getConf({'time':timeThr,
                              'charge':chargeThr},
                             self.gains)

        for i in range(17):
            key = f"{i+9:08x}".upper()
            val = f"{self.cConf[key]}".upper()

            self.tblOutput.setItem(i , 0, QTableWidgetItem(f"0x{key}"))
            self.tblOutput.setItem(i , 1, QTableWidgetItem(f"0x{val}"))

    def genConfGroup(self, timeThr, chargeThr):
        tr1Gains = [float(self.cmbTR1HG.currentText()),
                    float(self.cmbTR1LG.currentText())]
        tr2Gains = [float(self.cmbTR2HG.currentText()),
                    float(self.cmbTR2LG.currentText())]
        ranGains = [float(self.cmbRANHG.currentText()),
                    float(self.cmbRANLG.currentText())]
        lysoGains = [float(self.cmbLYSOHG.currentText()),
                     float(self.cmbLYSOLG.currentText())]
        latbotGains =  [float(self.cmbLATBOTHG.currentText()),
                        float(self.cmbLATBOTLG.currentText())]

        for i in range(5):
            self.gains[f'ch{i:02d}']['hg'] = tr1Gains[0]
            self.gains[f'ch{i:02d}']['lg'] = tr1Gains[1]

        for i in range(5,9):
            self.gains[f'ch{i:02d}']['hg'] = tr2Gains[0]
            self.gains[f'ch{i:02d}']['lg'] = tr2Gains[1]            

        for i in range(9,21):
            self.gains[f'ch{i:02d}']['hg'] = ranGains[0]
            self.gains[f'ch{i:02d}']['lg'] = ranGains[1]            

        for i in range(21,27):
            self.gains[f'ch{i:02d}']['hg'] = lysoGains[0]
            self.gains[f'ch{i:02d}']['lg'] = lysoGains[1]            

        for i in range(27,32):
            self.gains[f'ch{i:02d}']['hg'] = latbotGains[0]
            self.gains[f'ch{i:02d}']['lg'] = latbotGains[1]

    def genConfChannels(self, timeThr, chargeThr):
        for i in range(32):
            hgGain = float(self.sChCmbHG[i].currentText())
            lgGain = float(self.sChCmbLG[i].currentText())
            inCalib = self.sChInCalib[i].currentText().lower()
            inCalib = inCalib if inCalib != 'none' else None
            enabled = not self.sChDisabled[i].isChecked()

            self.gains[f'ch{i:02d}']['hg'] = hgGain
            self.gains[f'ch{i:02d}']['lg'] = lgGain
            self.gains[f'ch{i:02d}']['inCalib'] = inCalib
            self.gains[f'ch{i:02d}']['enabled'] = enabled

    def copyToClipboard(self):
        if self.cConf is None:
            self.errorMsg()
            return

        clipTxt = "03"        
        for v in self.cConf.values():
            clipTxt += f" {v}"

        self.clipboard.setText(clipTxt.upper())

    def saveToFile(self):
        if self.cConf is None:
            self.errorMsg()
            return

        fileName, fileType = QFileDialog.getSaveFileName(filter="Text files (*.txt)")

        if fileName == '':
            return

        with open(fileName,"w") as f:
            for v in self.cConf.values():
                f.write(f"0x{v.upper()}\n")

    def errorMsg(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Generate the configuration before proceeding!")
        msg.setWindowTitle("Configuration not generated!")
        msg.setStandardButtons(QMessageBox.Ok)

        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    clipBoard = QApplication.clipboard()

    win = mainWin(clipBoard)
    
    win.show()
    
    sys.exit(app.exec())