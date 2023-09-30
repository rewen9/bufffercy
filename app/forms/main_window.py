# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
# Импортируйте необходимые модули
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel

import core as core

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(513, 588)
        Frame.setMinimumSize(QtCore.QSize(300, 300))
        Frame.setWindowOpacity(1)
        self.checkBox = QtWidgets.QCheckBox(Frame)
        self.checkBox.setGeometry(QtCore.QRect(0, 540, 311, 28))
        self.checkBox.setObjectName("checkBox")
        self.tableView = QtWidgets.QTableView(Frame)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 511, 531))
        self.tableView.setDragEnabled(True)
        self.tableView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableView.setObjectName("tableView")
        
        self.model_tableView = QStandardItemModel()
        self.tableView.setModel(self.model_tableView)
        self.tableView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        
        
        self.Clipboard_manager = core.clipboard.clipboardManager()
        self.tableView.customContextMenuRequested.connect(
            self.copy_text_to_clipboard
            )
        
        # тестовая кнопка
        self.btn_test = QtWidgets.QPushButton(Frame)
        self.btn_test.setGeometry(QtCore.QRect(300, 540, 110, 40))
        self.btn_test.setObjectName("btn_test")
        self.btn_test.clicked.connect(self.addItem)
        
        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)
        self.is_install_xclip = False
        
        
    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "bufercy"))
        self.checkBox.setText(_translate("Frame", "Заполнять из буфера обмена"))
        self.btn_test.setText(_translate("Frame", "PushButton"))
    
    def addItem(self) -> None:
        """ Добавить строку в таблицу"""
        _text_buffer = self.Clipboard_manager.get_object_from_clipboard()
        if _text_buffer:
            row = [
                QStandardItem(_text_buffer),
            ]
            self.model_tableView.appendRow(row)
            # Set the width of self.tableView to 600 pixels
            self.tableView.setGeometry(QtCore.QRect(0, 0, 600, self.tableView.height()))
            self.tableView.setColumnWidth(0, 600)
    
    def copy_text_to_clipboard(self) -> None:
        """ Копирование текста в буфер обмена из QT"""
        index = self.tableView.currentIndex()
        model = self.tableView.model()
        text = model.data(index, QtCore.Qt.DisplayRole)
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(text)