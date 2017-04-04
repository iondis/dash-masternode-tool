# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/wnd_send_payout_base.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DialogSendPayout(object):
    def setupUi(self, DialogSendPayout):
        DialogSendPayout.setObjectName("DialogSendPayout")
        DialogSendPayout.resize(632, 444)
        DialogSendPayout.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogSendPayout)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(DialogSendPayout)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 8, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chbHideCollateralTx = QtWidgets.QCheckBox(DialogSendPayout)
        self.chbHideCollateralTx.setObjectName("chbHideCollateralTx")
        self.horizontalLayout.addWidget(self.chbHideCollateralTx)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableView = QtWidgets.QTableView(DialogSendPayout)
        self.tableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setShowGrid(True)
        self.tableView.setSortingEnabled(False)
        self.tableView.setObjectName("tableView")
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.verticalHeader().setCascadingSectionResizes(True)
        self.tableView.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 4, -1, 4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblAmountText = QtWidgets.QLabel(DialogSendPayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAmountText.sizePolicy().hasHeightForWidth())
        self.lblAmountText.setSizePolicy(sizePolicy)
        self.lblAmountText.setObjectName("lblAmountText")
        self.horizontalLayout_2.addWidget(self.lblAmountText)
        self.lblAmount = QtWidgets.QLabel(DialogSendPayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAmount.sizePolicy().hasHeightForWidth())
        self.lblAmount.setSizePolicy(sizePolicy)
        self.lblAmount.setObjectName("lblAmount")
        self.horizontalLayout_2.addWidget(self.lblAmount)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(DialogSendPayout)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.edtDestAddress = QtWidgets.QLineEdit(DialogSendPayout)
        self.edtDestAddress.setObjectName("edtDestAddress")
        self.horizontalLayout_4.addWidget(self.edtDestAddress)
        self.label_2 = QtWidgets.QLabel(DialogSendPayout)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.edtTxFee = QtWidgets.QDoubleSpinBox(DialogSendPayout)
        self.edtTxFee.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edtTxFee.setDecimals(5)
        self.edtTxFee.setMaximum(1.0)
        self.edtTxFee.setSingleStep(0.0001)
        self.edtTxFee.setObjectName("edtTxFee")
        self.horizontalLayout_4.addWidget(self.edtTxFee)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.btnSend = QtWidgets.QPushButton(DialogSendPayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy)
        self.btnSend.setMinimumSize(QtCore.QSize(200, 0))
        self.btnSend.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnSend.setAutoDefault(False)
        self.btnSend.setObjectName("btnSend")
        self.horizontalLayout_3.addWidget(self.btnSend)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.btnClose = QtWidgets.QPushButton(DialogSendPayout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMinimumSize(QtCore.QSize(0, 0))
        self.btnClose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnClose.setAutoDefault(False)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_3.addWidget(self.btnClose, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(DialogSendPayout)
        QtCore.QMetaObject.connectSlotsByName(DialogSendPayout)

    def retranslateUi(self, DialogSendPayout):
        _translate = QtCore.QCoreApplication.translate
        DialogSendPayout.setWindowTitle(_translate("DialogSendPayout", "Dialog"))
        self.label_3.setText(_translate("DialogSendPayout", "List of unspend transaction outputs (UTXO) assigned to Masternode addresses. You can transfer all or selected outputs to a new Dash address."))
        self.chbHideCollateralTx.setText(_translate("DialogSendPayout", "Hide collateral utxos"))
        self.lblAmountText.setText(_translate("DialogSendPayout", "Amount to send:"))
        self.lblAmount.setText(_translate("DialogSendPayout", "0"))
        self.label.setText(_translate("DialogSendPayout", "Send to address:"))
        self.label_2.setText(_translate("DialogSendPayout", "Fee (Dash):"))
        self.btnSend.setText(_translate("DialogSendPayout", "Send"))
        self.btnClose.setText(_translate("DialogSendPayout", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSendPayout = QtWidgets.QDialog()
    ui = Ui_DialogSendPayout()
    ui.setupUi(DialogSendPayout)
    DialogSendPayout.show()
    sys.exit(app.exec_())

