# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Project\QuantStudio\QuantStudio\Tools\QtGUI\DateTimeSetup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 590)
        Dialog.setSizeGripEnabled(True)
        self.gridLayout_4 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.FDBGroupBox = QtWidgets.QGroupBox(Dialog)
        self.FDBGroupBox.setObjectName("FDBGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.FDBGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_18 = QtWidgets.QLabel(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 2)
        self.StartDTEdit = QtWidgets.QDateTimeEdit(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartDTEdit.sizePolicy().hasHeightForWidth())
        self.StartDTEdit.setSizePolicy(sizePolicy)
        self.StartDTEdit.setObjectName("StartDTEdit")
        self.gridLayout.addWidget(self.StartDTEdit, 0, 2, 1, 3)
        self.label_21 = QtWidgets.QLabel(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 1, 0, 1, 2)
        self.EndDTEdit = QtWidgets.QDateTimeEdit(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EndDTEdit.sizePolicy().hasHeightForWidth())
        self.EndDTEdit.setSizePolicy(sizePolicy)
        self.EndDTEdit.setObjectName("EndDTEdit")
        self.gridLayout.addWidget(self.EndDTEdit, 1, 2, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 0, 1, 1)
        self.FactorComboBox = QtWidgets.QComboBox(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FactorComboBox.sizePolicy().hasHeightForWidth())
        self.FactorComboBox.setSizePolicy(sizePolicy)
        self.FactorComboBox.setObjectName("FactorComboBox")
        self.gridLayout.addWidget(self.FactorComboBox, 3, 1, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 3, 3, 1, 1)
        self.IDEdit = QtWidgets.QLineEdit(self.FDBGroupBox)
        self.IDEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.IDEdit.setObjectName("IDEdit")
        self.gridLayout.addWidget(self.IDEdit, 3, 4, 1, 1)
        self.FDTSelectTypeComboBox = QtWidgets.QComboBox(self.FDBGroupBox)
        self.FDTSelectTypeComboBox.setObjectName("FDTSelectTypeComboBox")
        self.FDTSelectTypeComboBox.addItem("")
        self.FDTSelectTypeComboBox.addItem("")
        self.FDTSelectTypeComboBox.addItem("")
        self.FDTSelectTypeComboBox.addItem("")
        self.FDTSelectTypeComboBox.addItem("")
        self.FDTSelectTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.FDTSelectTypeComboBox, 4, 1, 1, 2)
        self.SelectFDBDTButton = QtWidgets.QPushButton(self.FDBGroupBox)
        self.SelectFDBDTButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.SelectFDBDTButton.setObjectName("SelectFDBDTButton")
        self.gridLayout.addWidget(self.SelectFDBDTButton, 4, 4, 1, 1)
        self.FTComboBox = QtWidgets.QComboBox(self.FDBGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FTComboBox.sizePolicy().hasHeightForWidth())
        self.FTComboBox.setSizePolicy(sizePolicy)
        self.FTComboBox.setObjectName("FTComboBox")
        self.gridLayout.addWidget(self.FTComboBox, 2, 1, 1, 4)
        self.gridLayout_4.addWidget(self.FDBGroupBox, 0, 0, 1, 1)
        self.DateTimeListWidget = QtWidgets.QListWidget(Dialog)
        self.DateTimeListWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.DateTimeListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.DateTimeListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.DateTimeListWidget.setObjectName("DateTimeListWidget")
        self.gridLayout_4.addWidget(self.DateTimeListWidget, 0, 1, 3, 1)
        self.DateSetupGroupBox = QtWidgets.QGroupBox(Dialog)
        self.DateSetupGroupBox.setObjectName("DateSetupGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.DateSetupGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.StartDateEdit = QtWidgets.QDateEdit(self.DateSetupGroupBox)
        self.StartDateEdit.setObjectName("StartDateEdit")
        self.gridLayout_2.addWidget(self.StartDateEdit, 0, 2, 1, 1)
        self.DatePeriodComboBox = QtWidgets.QComboBox(self.DateSetupGroupBox)
        self.DatePeriodComboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DatePeriodComboBox.setObjectName("DatePeriodComboBox")
        self.gridLayout_2.addWidget(self.DatePeriodComboBox, 4, 2, 1, 1)
        self.DateListWidget = QtWidgets.QListWidget(self.DateSetupGroupBox)
        self.DateListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.DateListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.DateListWidget.setObjectName("DateListWidget")
        self.gridLayout_2.addWidget(self.DateListWidget, 0, 3, 7, 1)
        self.label_15 = QtWidgets.QLabel(self.DateSetupGroupBox)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)
        self.SelectDateButton = QtWidgets.QPushButton(self.DateSetupGroupBox)
        self.SelectDateButton.setMaximumSize(QtCore.QSize(88, 16777215))
        self.SelectDateButton.setObjectName("SelectDateButton")
        self.gridLayout_2.addWidget(self.SelectDateButton, 5, 2, 1, 1)
        self.EndDateEdit = QtWidgets.QDateEdit(self.DateSetupGroupBox)
        self.EndDateEdit.setObjectName("EndDateEdit")
        self.gridLayout_2.addWidget(self.EndDateEdit, 1, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.DateSetupGroupBox)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.DateSetupGroupBox)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.DateSetupGroupBox)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.DateSetupGroupBox)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 0, 1, 1)
        self.DateTypeComboBox = QtWidgets.QComboBox(self.DateSetupGroupBox)
        self.DateTypeComboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.DateTypeComboBox.setObjectName("DateTypeComboBox")
        self.gridLayout_2.addWidget(self.DateTypeComboBox, 2, 2, 1, 1)
        self.ExchangeEdit = QtWidgets.QLineEdit(self.DateSetupGroupBox)
        self.ExchangeEdit.setObjectName("ExchangeEdit")
        self.gridLayout_2.addWidget(self.ExchangeEdit, 3, 2, 1, 1)
        self.DateSelectTypeComboBox = QtWidgets.QComboBox(self.DateSetupGroupBox)
        self.DateSelectTypeComboBox.setObjectName("DateSelectTypeComboBox")
        self.DateSelectTypeComboBox.addItem("")
        self.DateSelectTypeComboBox.addItem("")
        self.DateSelectTypeComboBox.addItem("")
        self.DateSelectTypeComboBox.addItem("")
        self.DateSelectTypeComboBox.addItem("")
        self.DateSelectTypeComboBox.addItem("")
        self.gridLayout_2.addWidget(self.DateSelectTypeComboBox, 5, 0, 1, 1)
        self.gridLayout_4.addWidget(self.DateSetupGroupBox, 1, 0, 1, 1)
        self.TimeSetupGroupBox = QtWidgets.QGroupBox(Dialog)
        self.TimeSetupGroupBox.setObjectName("TimeSetupGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.TimeSetupGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(self.TimeSetupGroupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 1)
        self.AMStartTimeEdit = QtWidgets.QTimeEdit(self.TimeSetupGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AMStartTimeEdit.sizePolicy().hasHeightForWidth())
        self.AMStartTimeEdit.setSizePolicy(sizePolicy)
        self.AMStartTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(9, 30, 0)))
        self.AMStartTimeEdit.setMaximumTime(QtCore.QTime(11, 59, 59))
        self.AMStartTimeEdit.setObjectName("AMStartTimeEdit")
        self.gridLayout_3.addWidget(self.AMStartTimeEdit, 0, 1, 1, 1)
        self.TimeListWidget = QtWidgets.QListWidget(self.TimeSetupGroupBox)
        self.TimeListWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.TimeListWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.TimeListWidget.setObjectName("TimeListWidget")
        self.gridLayout_3.addWidget(self.TimeListWidget, 0, 2, 6, 1)
        self.label_19 = QtWidgets.QLabel(self.TimeSetupGroupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)
        self.AMEndTimeEdit = QtWidgets.QTimeEdit(self.TimeSetupGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AMEndTimeEdit.sizePolicy().hasHeightForWidth())
        self.AMEndTimeEdit.setSizePolicy(sizePolicy)
        self.AMEndTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(11, 30, 0)))
        self.AMEndTimeEdit.setMaximumTime(QtCore.QTime(11, 59, 59))
        self.AMEndTimeEdit.setObjectName("AMEndTimeEdit")
        self.gridLayout_3.addWidget(self.AMEndTimeEdit, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.TimeSetupGroupBox)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 2, 0, 1, 1)
        self.PMStartTimeEdit = QtWidgets.QTimeEdit(self.TimeSetupGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PMStartTimeEdit.sizePolicy().hasHeightForWidth())
        self.PMStartTimeEdit.setSizePolicy(sizePolicy)
        self.PMStartTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(13, 0, 0)))
        self.PMStartTimeEdit.setMinimumTime(QtCore.QTime(12, 0, 0))
        self.PMStartTimeEdit.setObjectName("PMStartTimeEdit")
        self.gridLayout_3.addWidget(self.PMStartTimeEdit, 2, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.TimeSetupGroupBox)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 3, 0, 1, 1)
        self.PMEndTimeEdit = QtWidgets.QTimeEdit(self.TimeSetupGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PMEndTimeEdit.sizePolicy().hasHeightForWidth())
        self.PMEndTimeEdit.setSizePolicy(sizePolicy)
        self.PMEndTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(15, 0, 0)))
        self.PMEndTimeEdit.setMinimumTime(QtCore.QTime(12, 0, 0))
        self.PMEndTimeEdit.setObjectName("PMEndTimeEdit")
        self.gridLayout_3.addWidget(self.PMEndTimeEdit, 3, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.TimeSetupGroupBox)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 4, 0, 1, 1)
        self.TimePeriodEdit = QtWidgets.QTimeEdit(self.TimeSetupGroupBox)
        self.TimePeriodEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 1, 0)))
        self.TimePeriodEdit.setMinimumTime(QtCore.QTime(0, 0, 1))
        self.TimePeriodEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.TimePeriodEdit.setObjectName("TimePeriodEdit")
        self.gridLayout_3.addWidget(self.TimePeriodEdit, 4, 1, 1, 1)
        self.SelectTimeButton = QtWidgets.QPushButton(self.TimeSetupGroupBox)
        self.SelectTimeButton.setMaximumSize(QtCore.QSize(88, 16777215))
        self.SelectTimeButton.setObjectName("SelectTimeButton")
        self.gridLayout_3.addWidget(self.SelectTimeButton, 5, 1, 1, 1)
        self.TimeSelectTypeComboBox = QtWidgets.QComboBox(self.TimeSetupGroupBox)
        self.TimeSelectTypeComboBox.setObjectName("TimeSelectTypeComboBox")
        self.TimeSelectTypeComboBox.addItem("")
        self.TimeSelectTypeComboBox.addItem("")
        self.TimeSelectTypeComboBox.addItem("")
        self.TimeSelectTypeComboBox.addItem("")
        self.TimeSelectTypeComboBox.addItem("")
        self.TimeSelectTypeComboBox.addItem("")
        self.gridLayout_3.addWidget(self.TimeSelectTypeComboBox, 5, 0, 1, 1)
        self.gridLayout_4.addWidget(self.TimeSetupGroupBox, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DTSelectTypeComboBox = QtWidgets.QComboBox(Dialog)
        self.DTSelectTypeComboBox.setObjectName("DTSelectTypeComboBox")
        self.DTSelectTypeComboBox.addItem("")
        self.DTSelectTypeComboBox.addItem("")
        self.DTSelectTypeComboBox.addItem("")
        self.DTSelectTypeComboBox.addItem("")
        self.DTSelectTypeComboBox.addItem("")
        self.DTSelectTypeComboBox.addItem("")
        self.horizontalLayout.addWidget(self.DTSelectTypeComboBox)
        self.SelectDTButton = QtWidgets.QPushButton(Dialog)
        self.SelectDTButton.setMaximumSize(QtCore.QSize(88, 16777215))
        self.SelectDTButton.setObjectName("SelectDTButton")
        self.horizontalLayout.addWidget(self.SelectDTButton)
        self.label_25 = QtWidgets.QLabel(Dialog)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout.addWidget(self.label_25)
        self.DateTimeNumEdit = QtWidgets.QLineEdit(Dialog)
        self.DateTimeNumEdit.setReadOnly(True)
        self.DateTimeNumEdit.setObjectName("DateTimeNumEdit")
        self.horizontalLayout.addWidget(self.DateTimeNumEdit)
        self.AcceptButton = QtWidgets.QPushButton(Dialog)
        self.AcceptButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AcceptButton.setObjectName("AcceptButton")
        self.horizontalLayout.addWidget(self.AcceptButton)
        self.RejectButton = QtWidgets.QPushButton(Dialog)
        self.RejectButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.RejectButton.setObjectName("RejectButton")
        self.horizontalLayout.addWidget(self.RejectButton)
        self.gridLayout_4.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.AcceptButton.raise_()
        self.RejectButton.raise_()
        self.DateSetupGroupBox.raise_()
        self.SelectDTButton.raise_()
        self.DateTimeListWidget.raise_()
        self.label_25.raise_()
        self.DateTimeNumEdit.raise_()
        self.TimeSetupGroupBox.raise_()
        self.DTSelectTypeComboBox.raise_()
        self.FDBGroupBox.raise_()
        self.label_18.setBuddy(self.StartDTEdit)
        self.label_21.setBuddy(self.EndDTEdit)
        self.label_11.setBuddy(self.FTComboBox)
        self.label_12.setBuddy(self.FactorComboBox)
        self.label_26.setBuddy(self.IDEdit)
        self.label_15.setBuddy(self.EndDateEdit)
        self.label_13.setBuddy(self.StartDateEdit)
        self.label_14.setBuddy(self.DatePeriodComboBox)
        self.label_16.setBuddy(self.DateTypeComboBox)
        self.label_17.setBuddy(self.ExchangeEdit)
        self.label_20.setBuddy(self.AMStartTimeEdit)
        self.label_19.setBuddy(self.AMEndTimeEdit)
        self.label_24.setBuddy(self.PMStartTimeEdit)
        self.label_22.setBuddy(self.PMEndTimeEdit)
        self.label_23.setBuddy(self.TimePeriodEdit)
        self.label_25.setBuddy(self.DateTimeNumEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "日期时间设置"))
        self.FDBGroupBox.setTitle(_translate("Dialog", "来自因子库"))
        self.label_18.setText(_translate("Dialog", "起始时点"))
        self.StartDTEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm:ss"))
        self.label_21.setText(_translate("Dialog", "终止时点"))
        self.EndDTEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd HH:mm:ss"))
        self.label_11.setText(_translate("Dialog", "因子表"))
        self.label_12.setText(_translate("Dialog", "因子"))
        self.label_26.setText(_translate("Dialog", "ID"))
        self.FDTSelectTypeComboBox.setItemText(0, _translate("Dialog", "覆盖"))
        self.FDTSelectTypeComboBox.setItemText(1, _translate("Dialog", "并集"))
        self.FDTSelectTypeComboBox.setItemText(2, _translate("Dialog", "交集"))
        self.FDTSelectTypeComboBox.setItemText(3, _translate("Dialog", "左差右"))
        self.FDTSelectTypeComboBox.setItemText(4, _translate("Dialog", "右差左"))
        self.FDTSelectTypeComboBox.setItemText(5, _translate("Dialog", "对称差"))
        self.SelectFDBDTButton.setText(_translate("Dialog", ">>"))
        self.DateSetupGroupBox.setTitle(_translate("Dialog", "日期设置"))
        self.StartDateEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
        self.label_15.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">终止日期</p></body></html>"))
        self.SelectDateButton.setText(_translate("Dialog", ">>"))
        self.EndDateEdit.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">起始日期</p></body></html>"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">日期周期</p></body></html>"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">日期类型</p></body></html>"))
        self.label_17.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">交易所</p></body></html>"))
        self.ExchangeEdit.setText(_translate("Dialog", "SSE"))
        self.DateSelectTypeComboBox.setItemText(0, _translate("Dialog", "覆盖"))
        self.DateSelectTypeComboBox.setItemText(1, _translate("Dialog", "并集"))
        self.DateSelectTypeComboBox.setItemText(2, _translate("Dialog", "交集"))
        self.DateSelectTypeComboBox.setItemText(3, _translate("Dialog", "左差右"))
        self.DateSelectTypeComboBox.setItemText(4, _translate("Dialog", "右差左"))
        self.DateSelectTypeComboBox.setItemText(5, _translate("Dialog", "对称差"))
        self.TimeSetupGroupBox.setTitle(_translate("Dialog", "时间设置"))
        self.label_20.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">AM 起始时间</p></body></html>"))
        self.AMStartTimeEdit.setDisplayFormat(_translate("Dialog", "HH:mm:ss"))
        self.label_19.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">AM 终止时间</p></body></html>"))
        self.AMEndTimeEdit.setDisplayFormat(_translate("Dialog", "HH:mm:ss"))
        self.label_24.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">PM 起始时间</p></body></html>"))
        self.PMStartTimeEdit.setDisplayFormat(_translate("Dialog", "HH:mm:ss"))
        self.label_22.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">PM 终止时间</p></body></html>"))
        self.PMEndTimeEdit.setDisplayFormat(_translate("Dialog", "HH:mm:ss"))
        self.label_23.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">时间周期</p></body></html>"))
        self.TimePeriodEdit.setDisplayFormat(_translate("Dialog", "HH:mm:ss"))
        self.SelectTimeButton.setText(_translate("Dialog", ">>"))
        self.TimeSelectTypeComboBox.setItemText(0, _translate("Dialog", "覆盖"))
        self.TimeSelectTypeComboBox.setItemText(1, _translate("Dialog", "并集"))
        self.TimeSelectTypeComboBox.setItemText(2, _translate("Dialog", "交集"))
        self.TimeSelectTypeComboBox.setItemText(3, _translate("Dialog", "左差右"))
        self.TimeSelectTypeComboBox.setItemText(4, _translate("Dialog", "右差左"))
        self.TimeSelectTypeComboBox.setItemText(5, _translate("Dialog", "对称差"))
        self.DTSelectTypeComboBox.setItemText(0, _translate("Dialog", "覆盖"))
        self.DTSelectTypeComboBox.setItemText(1, _translate("Dialog", "并集"))
        self.DTSelectTypeComboBox.setItemText(2, _translate("Dialog", "交集"))
        self.DTSelectTypeComboBox.setItemText(3, _translate("Dialog", "左差右"))
        self.DTSelectTypeComboBox.setItemText(4, _translate("Dialog", "右差左"))
        self.DTSelectTypeComboBox.setItemText(5, _translate("Dialog", "对称差"))
        self.SelectDTButton.setText(_translate("Dialog", ">>"))
        self.label_25.setText(_translate("Dialog", "时点数"))
        self.DateTimeNumEdit.setText(_translate("Dialog", "0"))
        self.AcceptButton.setText(_translate("Dialog", "确定"))
        self.RejectButton.setText(_translate("Dialog", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

