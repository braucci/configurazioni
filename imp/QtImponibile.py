#!/usr/bin/python
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6 import uic

class Ui(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('/home/biagio/.config/polybar/imp/imponibile.ui', self)
        self.setFixedSize(399, 177)
    

    def pB_valutaClick(self):

        def imponibile(n1,n2):
            n3 = n1*100/(n2+100)
            return n3
        
        def iva(n1, n3):
            n4 = n1-n3
            return n4

        
        try:
            n1 = float(self.lE_totFattura.text())
            n2 = float(self.lE_aliquota.text())
            
            impvalue = imponibile(n1,n2)
            ivavalue = iva(n1,impvalue)

            self.lE_imponibile.setText(str(format(impvalue,'>12.2f')))
            self.lE_iva.setText(str(format(ivavalue,'>12.2f')))
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