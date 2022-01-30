#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('imponibile.ui', self)
        self.setFixedSize(399, 177)

    def pB_valutaClick(self):
        try:
            n1 = float(self.lE_totFattura.text())
            n2 = float(self.lE_aliquota.text())
            n3 = n1*100/(n2+100)
            n4 = n1-n3
            self.lE_imponibile.setText(str(format(n3,'>12.2f')))
            self.lE_iva.setText(str(format(n4,'>12.2f')))
            self.l_errore.setText('')
        except:
            self.l_errore.setText('Valore numerico non accettato')
            self.lE_imponibile.setText('')
            self.lE_iva.setText('')
            self.lE_aliquota.setText('22')



app = QApplication([])
window = Ui()
window.show()
app.exec()