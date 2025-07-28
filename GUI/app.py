from PySide6 import QtCore, QtWidgets

from GUI.template import HistoryChoiceWidget

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(800, 600)
    centralwidget = QtWidgets.QWidget(MainWindow)
    centralwidget.setObjectName("centralwidget")
    # horizontalLayout = QtWidgets.QHBoxLayout(centralwidget)
    # horizontalLayout.setObjectName("horizontalLayout")
    groupBox = HistoryChoiceWidget(centralwidget)
    groupBox.setObjectName("groupBox")
    # horizontalLayout.addWidget(groupBox)
    MainWindow.setCentralWidget(centralwidget)
    # menubar = QtWidgets.QMenuBar(MainWindow)
    # menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
    # menubar.setObjectName("menubar")
    # MainWindow.setMenuBar(menubar)
    # statusbar = QtWidgets.QStatusBar(MainWindow)
    # statusbar.setObjectName("statusbar")
    # MainWindow.setStatusBar(statusbar)
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    # groupBox.setTitle(_translate("MainWindow", "GroupBox"))
    MainWindow.show()
    sys.exit(app.exec())

# """
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# MainWindow.setObjectName("MainWindow")
# MainWindow.resize(1111, 777)
# centralwidget = QtWidgets.QWidget(MainWindow)
# centralwidget.setObjectName("centralwidget")
# # Layout = QtWidgets.QHBoxLayout(centralwidget)
# widget = HistoryChoiceWidget(centralwidget)
# # Layout.addWidget(widget)
# """
