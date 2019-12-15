import networkx as nx
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from TokyoInterfazUI import Ui_MainWindow
import Algoritmo
import Grafo
from VentanaAuxUI import Ui_MainWindow2


def listToString(s):
    # initialize an empty string
    str1 = "\n".join(s)
    return str1


class window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.setupUi(self)
        self.CalcularRuta.clicked.connect(self.on_PushButtonFirst_clicked)
        self.partnerDialog = Window2(self)

    def on_PushButtonFirst_clicked(self):
        self.partnerDialog.ruta.setText(self.pressed())
        self.partnerDialog.show()

    def pressed(self):
        x = self.comboOrigen.currentText()
        y = self.comboDestino.currentText()
        z = Grafo.G
        e = Algoritmo.astar(x, y)
        eString = listToString(e)
        return eString


class Window2(QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None):
        super(Window2, self).__init__(parent)
        self.setupUi(self)
        self.OkButton.clicked.connect(self.close_window2)

    def close_window2(self):
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    gui = window()
    gui.show()
    app.exec_()
