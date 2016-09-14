import sys 
from PyQt4 import QtGui, QtCore
import datetime

class Viva(QtGui.QWidget):

  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.label = QtGui.QLabel('Personajes importantes de la independencia' + '\n' + '1.- Jose Maria Morelos y Pavon'+ '\n' + '2.- Josefa Ortiz de Dominguez'+ '\n' + '3.- Miguel Hidalgo', self)
    boton = QtGui.QPushButton('Aprietame', self)
    mexico = QtGui.QIcon("mex.png")

    boton.clicked.connect(lambda: boton.setText("Faltan " + str(calc())+ " dias"))

    self.label.move(40,40)
    boton.move(40, 200)
    boton.setFixedSize(200,50)

    self.setGeometry(200, 200, 400, 300)
    self.setWindowTitle('¡Viva México!')
    self.setWindowIcon(mexico)
    self.show()

def calc():
  now = datetime.date.today()
  independence = datetime.date(now.year,9,15)
  independenceb = datetime.date(now.year+1,9,15)
  if now.month >= 9 and now.day >= 15:
    days = (independenceb-now).days
  else:
    days = (independence-now).days
  return days;

def main():
  app = QtGui.QApplication(sys.argv)
  vi = Viva()
  sys.exit(app.exec_())


if __name__ == '__main__':
  main()