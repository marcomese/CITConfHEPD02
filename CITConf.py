#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem,
                             QLabel, QHBoxLayout, QComboBox,
                             QCheckBox, QFileDialog)
from mainGUI import Ui_MainWindow
from citSupportLib import HGValidGains, LGValidGains
from getCITConfig import getConf, defGains

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
        cmb.addItems([str(v) for v in validGains])
        cmb.setCurrentIndex(validGains.index(defGain))

    def initGroupTab(self):
        self.initComboBox(self.cmbTR1HG, HGValidGains, 75.0)
        self.initComboBox(self.cmbTR1LG, LGValidGains, 7.5)
        self.initComboBox(self.cmbTR2HG, HGValidGains, 75.0)
        self.initComboBox(self.cmbTR2LG, LGValidGains, 7.5)
        self.initComboBox(self.cmbRANHG, HGValidGains, 75.0)
        self.initComboBox(self.cmbRANLG, LGValidGains, 7.5)
        self.initComboBox(self.cmbLYSOHG, HGValidGains, 10.0)
        self.initComboBox(self.cmbLYSOLG, LGValidGains, 1.5)
        self.initComboBox(self.cmbLATBOTHG, HGValidGains, 75.0)
        self.initComboBox(self.cmbLATBOTLG, LGValidGains, 7.5)

    def initSingleChTab(self):
        self.hLaySingleCh = []
        self.sChLabels    = []
        self.sChCmbHG     = []
        self.sChCmbLG     = []
        self.sChInCalib   = []
        self.sChDisabled  = []
        for i in range(32):
            initValHG = 75.0 if (i < 21 or i > 26) else 10.0
            initValLG = 7.5 if (i < 21 or i > 26) else 1.5

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
            return

        clipTxt = "03"        
        for v in self.cConf.values():
            clipTxt += f" {v}"

        self.clipboard.setText(clipTxt.upper())

    def saveToFile(self):
        fileName, fileType = QFileDialog.getSaveFileName(filter="Text files (*.txt)")

        with open(fileName,"w") as f:
            for v in self.cConf.values():
                f.write(f"0x{v.upper()}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    clipBoard = QApplication.clipboard()

    win = mainWin(clipBoard)
    
    win.show()
    
    sys.exit(app.exec())