import sys
from PyQt5 import QtCore, QtGui, QtWidgets
app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()
w.resize(250, 150)
w.move(300, 300)
w.setWindowTitle('hello python unittest')
w.show()
sys.exit(app.exec_())
