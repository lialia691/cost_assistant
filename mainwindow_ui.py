# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_form(object):
    def setupUi(self, form):
        if not form.objectName():
            form.setObjectName(u"form")
        form.resize(908, 636)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form.sizePolicy().hasHeightForWidth())
        form.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        form.setFont(font)
        self.verticalLayout_5 = QVBoxLayout(form)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_14)

        self.groupBox_2 = QGroupBox(form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setKerning(True)
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.checkBox_gushi_house = QCheckBox(self.groupBox_2)
        self.checkBox_gushi_house.setObjectName(u"checkBox_gushi_house")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkBox_gushi_house.sizePolicy().hasHeightForWidth())
        self.checkBox_gushi_house.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.checkBox_gushi_house, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_gushi_house_period = QComboBox(self.groupBox_2)
        self.comboBox_gushi_house_period.addItem("")
        self.comboBox_gushi_house_period.addItem("")
        self.comboBox_gushi_house_period.setObjectName(u"comboBox_gushi_house_period")
        sizePolicy2.setHeightForWidth(self.comboBox_gushi_house_period.sizePolicy().hasHeightForWidth())
        self.comboBox_gushi_house_period.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.comboBox_gushi_house_period, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignLeft)

        self.checkBox_xinyang_house = QCheckBox(self.groupBox_2)
        self.checkBox_xinyang_house.setObjectName(u"checkBox_xinyang_house")
        sizePolicy2.setHeightForWidth(self.checkBox_xinyang_house.sizePolicy().hasHeightForWidth())
        self.checkBox_xinyang_house.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.checkBox_xinyang_house, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_xinyang_house_period = QComboBox(self.groupBox_2)
        self.comboBox_xinyang_house_period.addItem("")
        self.comboBox_xinyang_house_period.setObjectName(u"comboBox_xinyang_house_period")
        sizePolicy2.setHeightForWidth(self.comboBox_xinyang_house_period.sizePolicy().hasHeightForWidth())
        self.comboBox_xinyang_house_period.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.comboBox_xinyang_house_period)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignLeft)

        self.checkBox_zhengzhou_house_month = QCheckBox(self.groupBox_2)
        self.checkBox_zhengzhou_house_month.setObjectName(u"checkBox_zhengzhou_house_month")
        sizePolicy2.setHeightForWidth(self.checkBox_zhengzhou_house_month.sizePolicy().hasHeightForWidth())
        self.checkBox_zhengzhou_house_month.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.checkBox_zhengzhou_house_month, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_zhengzhou_house_mperiod = QComboBox(self.groupBox_2)
        self.comboBox_zhengzhou_house_mperiod.addItem("")
        self.comboBox_zhengzhou_house_mperiod.setObjectName(u"comboBox_zhengzhou_house_mperiod")
        sizePolicy2.setHeightForWidth(self.comboBox_zhengzhou_house_mperiod.sizePolicy().hasHeightForWidth())
        self.comboBox_zhengzhou_house_mperiod.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.comboBox_zhengzhou_house_mperiod)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignLeft)

        self.checkBox_zhengzhou_house_quarter = QCheckBox(self.groupBox_2)
        self.checkBox_zhengzhou_house_quarter.setObjectName(u"checkBox_zhengzhou_house_quarter")
        sizePolicy2.setHeightForWidth(self.checkBox_zhengzhou_house_quarter.sizePolicy().hasHeightForWidth())
        self.checkBox_zhengzhou_house_quarter.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.checkBox_zhengzhou_house_quarter, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_zhengzhou_house_qperiod = QComboBox(self.groupBox_2)
        self.comboBox_zhengzhou_house_qperiod.addItem("")
        self.comboBox_zhengzhou_house_qperiod.setObjectName(u"comboBox_zhengzhou_house_qperiod")
        sizePolicy2.setHeightForWidth(self.comboBox_zhengzhou_house_qperiod.sizePolicy().hasHeightForWidth())
        self.comboBox_zhengzhou_house_qperiod.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.comboBox_zhengzhou_house_qperiod)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)

        self.horizontalLayout_10.addWidget(self.label_6, 0, Qt.AlignmentFlag.AlignLeft)

        self.checkBox_other_house = QCheckBox(self.groupBox_2)
        self.checkBox_other_house.setObjectName(u"checkBox_other_house")
        sizePolicy2.setHeightForWidth(self.checkBox_other_house.sizePolicy().hasHeightForWidth())
        self.checkBox_other_house.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.checkBox_other_house, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_other_house_qperiod = QComboBox(self.groupBox_2)
        self.comboBox_other_house_qperiod.addItem("")
        self.comboBox_other_house_qperiod.setObjectName(u"comboBox_other_house_qperiod")
        sizePolicy2.setHeightForWidth(self.comboBox_other_house_qperiod.sizePolicy().hasHeightForWidth())
        self.comboBox_other_house_qperiod.setSizePolicy(sizePolicy2)

        self.horizontalLayout_10.addWidget(self.comboBox_other_house_qperiod)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(form)
        self.groupBox.setObjectName(u"groupBox")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.groupBox.setFont(font2)
        self.groupBox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.label_9)

        self.checkBox_xinyang_road = QCheckBox(self.groupBox)
        self.checkBox_xinyang_road.setObjectName(u"checkBox_xinyang_road")
        sizePolicy2.setHeightForWidth(self.checkBox_xinyang_road.sizePolicy().hasHeightForWidth())
        self.checkBox_xinyang_road.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.checkBox_xinyang_road, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_xinyang_road_period = QComboBox(self.groupBox)
        self.comboBox_xinyang_road_period.addItem("")
        self.comboBox_xinyang_road_period.setObjectName(u"comboBox_xinyang_road_period")
        sizePolicy2.setHeightForWidth(self.comboBox_xinyang_road_period.sizePolicy().hasHeightForWidth())
        self.comboBox_xinyang_road_period.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.comboBox_xinyang_road_period, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.checkBox_zhengzhou_road = QCheckBox(self.groupBox)
        self.checkBox_zhengzhou_road.setObjectName(u"checkBox_zhengzhou_road")
        sizePolicy2.setHeightForWidth(self.checkBox_zhengzhou_road.sizePolicy().hasHeightForWidth())
        self.checkBox_zhengzhou_road.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.checkBox_zhengzhou_road, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_zhengzhou_road_period = QComboBox(self.groupBox)
        self.comboBox_zhengzhou_road_period.addItem("")
        self.comboBox_zhengzhou_road_period.setObjectName(u"comboBox_zhengzhou_road_period")
        sizePolicy2.setHeightForWidth(self.comboBox_zhengzhou_road_period.sizePolicy().hasHeightForWidth())
        self.comboBox_zhengzhou_road_period.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.comboBox_zhengzhou_road_period, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.label_10)

        self.checkBox_other_road = QCheckBox(self.groupBox)
        self.checkBox_other_road.setObjectName(u"checkBox_other_road")
        sizePolicy2.setHeightForWidth(self.checkBox_other_road.sizePolicy().hasHeightForWidth())
        self.checkBox_other_road.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.checkBox_other_road, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_other_road_period = QComboBox(self.groupBox)
        self.comboBox_other_road_period.addItem("")
        self.comboBox_other_road_period.setObjectName(u"comboBox_other_road_period")
        sizePolicy2.setHeightForWidth(self.comboBox_other_road_period.sizePolicy().hasHeightForWidth())
        self.comboBox_other_road_period.setSizePolicy(sizePolicy2)

        self.horizontalLayout_11.addWidget(self.comboBox_other_road_period, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_12)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer_13)


        self.horizontalLayout_4.addWidget(self.groupBox)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.lineEdit = QLineEdit(form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(200, 40))
        self.lineEdit.setStyleSheet(u"font: 14pt \"Microsoft YaHei UI\";")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.pushButton = QPushButton(form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setSizeIncrement(QSize(0, 0))
        self.pushButton.setBaseSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setKerning(True)
        self.pushButton.setFont(font3)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(887, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frame = QFrame(form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableView = QTableView(self.frame)
        self.tableView.setObjectName(u"tableView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy3)

        self.verticalLayout_3.addWidget(self.tableView)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_total_records = QLabel(self.frame)
        self.label_total_records.setObjectName(u"label_total_records")

        self.horizontalLayout_7.addWidget(self.label_total_records)

        self.label_current_page = QLabel(self.frame)
        self.label_current_page.setObjectName(u"label_current_page")

        self.horizontalLayout_7.addWidget(self.label_current_page)

        self.pushButton_next = QPushButton(self.frame)
        self.pushButton_next.setObjectName(u"pushButton_next")

        self.horizontalLayout_7.addWidget(self.pushButton_next)

        self.pushButton_previous = QPushButton(self.frame)
        self.pushButton_previous.setObjectName(u"pushButton_previous")

        self.horizontalLayout_7.addWidget(self.pushButton_previous)

        self.pushButton_home = QPushButton(self.frame)
        self.pushButton_home.setObjectName(u"pushButton_home")

        self.horizontalLayout_7.addWidget(self.pushButton_home)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_9 = QSpacerItem(771, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.horizontalSpacer_9)


        self.horizontalLayout_12.addWidget(self.frame)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.groupBox_2.raise_()
        self.groupBox.raise_()

        self.retranslateUi(form)

        QMetaObject.connectSlotsByName(form)
    # setupUi

    def retranslateUi(self, form):
        form.setWindowTitle(QCoreApplication.translate("form", u"\u6750\u6599\u4ef7\u52a9\u624b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("form", u"\u623f\u5efa\u4fe1\u606f\u4ef7", None))
        self.label.setText(QCoreApplication.translate("form", u"\u56fa\u59cb\u623f\u5efa", None))
        self.checkBox_gushi_house.setText("")
        self.comboBox_gushi_house_period.setItemText(0, QCoreApplication.translate("form", u"\u56fa\u59cb2024\u5e74\u7b2c2\u671f", None))
        self.comboBox_gushi_house_period.setItemText(1, QCoreApplication.translate("form", u"\u56fa\u59cb2024\u5e74\u7b2c1\u671f", None))

        self.label_3.setText(QCoreApplication.translate("form", u"\u4fe1\u9633\u623f\u5efa", None))
        self.checkBox_xinyang_house.setText("")
        self.comboBox_xinyang_house_period.setItemText(0, QCoreApplication.translate("form", u"\u4fe1\u96332024\u5e74\u7b2c1\u671f", None))

        self.label_4.setText(QCoreApplication.translate("form", u"\u90d1\u5dde\u623f\u5efa\u6708\u4efd\u4ef7", None))
        self.checkBox_zhengzhou_house_month.setText("")
        self.comboBox_zhengzhou_house_mperiod.setItemText(0, QCoreApplication.translate("form", u"\u90d1\u5dde2024\u5e743\u6708", None))

        self.label_5.setText(QCoreApplication.translate("form", u"\u90d1\u5dde\u623f\u5efa\u5b63\u5ea6\u4ef7", None))
        self.checkBox_zhengzhou_house_quarter.setText("")
        self.comboBox_zhengzhou_house_qperiod.setItemText(0, QCoreApplication.translate("form", u"\u90d1\u5dde2024\u5e741\u5b63\u5ea6", None))

        self.label_6.setText(QCoreApplication.translate("form", u"\u5176\u4ed6\u5730\u533a\u623f\u5efa\u4fe1\u606f\u4ef7", None))
        self.checkBox_other_house.setText("")
        self.comboBox_other_house_qperiod.setItemText(0, "")

        self.groupBox.setTitle(QCoreApplication.translate("form", u"\u516c\u8def\u4fe1\u606f\u4ef7", None))
        self.label_9.setText(QCoreApplication.translate("form", u"\u4fe1\u9633\u516c\u8def", None))
        self.checkBox_xinyang_road.setText("")
        self.comboBox_xinyang_road_period.setItemText(0, QCoreApplication.translate("form", u"\u4fe1\u9633\u516c\u8def2024\u5e743\u6708", None))

        self.label_8.setText(QCoreApplication.translate("form", u"\u90d1\u5dde\u516c\u8def", None))
        self.checkBox_zhengzhou_road.setText("")
        self.comboBox_zhengzhou_road_period.setItemText(0, QCoreApplication.translate("form", u"\u90d1\u5dde\u516c\u8def2024\u5e743\u6708", None))

        self.label_10.setText(QCoreApplication.translate("form", u"\u5176\u4ed6\u5730\u533a\u516c\u8def", None))
        self.checkBox_other_road.setText("")
        self.comboBox_other_road_period.setItemText(0, "")

        self.pushButton.setText(QCoreApplication.translate("form", u"\u67e5\u8be2", None))
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("form", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_total_records.setText(QCoreApplication.translate("form", u"\u603b\u8bb0\u5f55\u6570: 0", None))
        self.label_current_page.setText(QCoreApplication.translate("form", u"\u5f53\u524d\u9875: 1", None))
        self.pushButton_next.setText(QCoreApplication.translate("form", u"\u4e0b\u4e00\u9875", None))
        self.pushButton_previous.setText(QCoreApplication.translate("form", u"\u4e0a\u4e00\u9875", None))
        self.pushButton_home.setText(QCoreApplication.translate("form", u"\u9996\u9875", None))
    # retranslateUi

