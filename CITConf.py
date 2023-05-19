#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from mainGUI import Ui_MainWindow
from citSupportLib import HGValidGains, LGValidGains
from getCITConfig import getConf, defGains

class mainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.gains = defGains
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.initComboBoxes(self.cmbBoxTR1HG, HGValidGains, 75.0)
        self.initComboBoxes(self.cmbBoxTR1LG, LGValidGains, 7.5)
        self.initComboBoxes(self.cmbBoxTR2HG, HGValidGains, 75.0)
        self.initComboBoxes(self.cmbBoxTR2LG, LGValidGains, 7.5)
        self.initComboBoxes(self.cmbBoxRANHG, HGValidGains, 75.0)
        self.initComboBoxes(self.cmbBoxRANLG, LGValidGains, 7.5)
        self.initComboBoxes(self.cmbBoxLYSOHG, HGValidGains, 10.0)
        self.initComboBoxes(self.cmbBoxLYSOLG, LGValidGains, 1.5)
        self.initComboBoxes(self.cmbBoxLATBOTHG, HGValidGains, 75.0)
        self.initComboBoxes(self.cmbBoxLATBOTLG, LGValidGains, 7.5)

        for i in range(17):
            self.tblOutput.insertRow(i)
            self.tblOutput.setItem(i , 0, QTableWidgetItem("0x"+f"{i+9:08x}".upper()))
        
        self.btnGen.clicked.connect(self.genConf)

    def initComboBoxes(self, cmb, validGains, defGain):
        cmb.addItems([str(v) for v in validGains])
        cmb.setCurrentIndex(validGains.index(defGain))

    def genConf(self):
        timeThr = int(self.txtTimeThr.text())
        chargeThr = int(self.txtChargeThr.text())
        
        tr1Gains = [float(self.cmbBoxTR1HG.currentText()),
                    float(self.cmbBoxTR1LG.currentText())]
        tr2Gains = [float(self.cmbBoxTR2HG.currentText()),
                    float(self.cmbBoxTR2LG.currentText())]
        ranGains = [float(self.cmbBoxRANHG.currentText()),
                    float(self.cmbBoxRANLG.currentText())]
        lysoGains = [float(self.cmbBoxLYSOHG.currentText()),
                     float(self.cmbBoxLYSOLG.currentText())]
        latbotGains =  [float(self.cmbBoxLATBOTHG.currentText()),
                        float(self.cmbBoxLATBOTLG.currentText())]

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

        cConf = getConf({'time':timeThr,'charge':chargeThr},
                        self.gains)

        for i in range(17):
            key = f"{i+9:08x}".upper()
            val = f"{cConf[key]}".upper()

            self.tblOutput.setItem(i , 0, QTableWidgetItem(f"0x{key}"))
            self.tblOutput.setItem(i , 1, QTableWidgetItem(f"0x{val}"))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = mainWin()
    
    win.show()
    
    sys.exit(app.exec())