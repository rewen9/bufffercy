# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(513, 588)
        Frame.setMinimumSize(QtCore.QSize(300, 300))
        Frame.setWindowOpacity(-14.0)
        self.checkBox = QtWidgets.QCheckBox(Frame)
        self.checkBox.setGeometry(QtCore.QRect(0, 540, 311, 28))
        self.checkBox.setObjectName("checkBox")
        self.tableView = QtWidgets.QTableView(Frame)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 511, 531))
        self.tableView.setDragEnabled(True)
        self.tableView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableView.setObjectName("tableView")
        self.btn_test = QtWidgets.QPushButton(Frame)
        self.btn_test.setGeometry(QtCore.QRect(300, 540, 110, 40))
        self.btn_test.setObjectName("btn_test")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "bufercy"))
        self.checkBox.setText(_translate("Frame", "Заполнять из буфера обмена"))
        self.btn_test.setText(_translate("Frame", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())