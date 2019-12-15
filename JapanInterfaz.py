from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from JapanInterfazUI import Ui_MainWindow
import Algoritmo
import Grafo
from VentanaAuxUI import Ui_MainWindow2

#Creamos una clase para cada ventana: JapanInterfazUI y VentanaAuxUI
class window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        #Iniciamos la ventana y sus caracteristicas
        self.setupUi(self)
        #Al hacer click en el boton calcular ruta empezamos el dialogo entre las dos ventanas
        self.CalcularRuta.clicked.connect(self.on_PushButtonFirst_clicked)
        self.partnerDialog = Window2(self)

    #Escribe en ruta el String devuelto por pressed
    def on_PushButtonFirst_clicked(self):
        self.partnerDialog.ruta.setText(self.pressed())
        self.partnerDialog.show()

    '''
    Devuelve un String con el camino calculado por
    astar para llegar de un origen a un destino
    '''
    def pressed(self):
        x = self.comboOrigen.currentText()
        y = self.comboDestino.currentText()
        z = Grafo.G
        e = Algoritmo.astar(x, y)
        eString = "\n".join(e)
        return eString


class Window2(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.setupUi(self)
        #Al hacer click en el boton ok cerramos la ventana
        self.OkButton.clicked.connect(self.close_window2)

    def close_window2(self):
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    gui = window()
    gui.show()
    app.exec_()
