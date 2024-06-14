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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(932, 741)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_5 = QSpacerItem(161, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(280, 0))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font.setPointSize(12)
        font.setBold(True)
        font.setKerning(True)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid gray; /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u548c\u5bbd\u5ea6 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2 */\n"
"    margin-top: 25px; /* \u8bbe\u7f6e\u6807\u9898\u4e0e\u5185\u5bb9\u7684\u95f4\u8ddd */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; /* \u6807\u9898\u4f4d\u7f6e */\n"
"    subcontrol-position: top center; /* \u6807\u9898\u5c45\u4e2d */\n"
"    padding: 0 3px; /* \u6807\u9898\u5185\u8fb9\u8ddd */   \n"
"}\n"
"")
        self.groupBox_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
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
        self.comboBox_gushi_house_period.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.comboBox_gushi_house_period.sizePolicy().hasHeightForWidth())
        self.comboBox_gushi_house_period.setSizePolicy(sizePolicy2)
        self.comboBox_gushi_house_period.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid lightgrey;\n"
"    padding: 3px;\n"
"}")

        self.horizontalLayout.addWidget(self.comboBox_gushi_house_period)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
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
        self.comboBox_xinyang_house_period.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid lightgrey;\n"
"    padding: 3px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.comboBox_xinyang_house_period)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.checkBox_zhengzhou_house_month = QCheckBox(self.groupBox_2)
        self.checkBox_zhengzhou_house_month.setObjectName(u"checkBox_zhengzhou_house_month")
        sizePolicy2.setHeightForWidth(self.checkBox_zhengzhou_house_month.sizePolicy().hasHeightForWidth())
        self.checkBox_zhengzhou_house_month.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.checkBox_zhengzhou_house_month, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_zhengzhou_house_mperiod = QComboBox(self.groupBox_2)
        self.comboBox_zhengzhou_house_mperiod.addItem("")
        self.comboBox_zhengzhou_house_mperiod.addItem("")
        self.comboBox_zhengzhou_house_mperiod.setObjectName(u"comboBox_zhengzhou_house_mperiod")
        sizePolicy2.setHeightForWidth(self.comboBox_zhengzhou_house_mperiod.sizePolicy().hasHeightForWidth())
        self.comboBox_zhengzhou_house_mperiod.setSizePolicy(sizePolicy2)
        self.comboBox_zhengzhou_house_mperiod.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid lightgrey;\n"
"    padding: 3px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.comboBox_zhengzhou_house_mperiod)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox_zhengzhou_house_quarter = QCheckBox(self.groupBox_2)
        self.checkBox_zhengzhou_house_quarter.setObjectName(u"checkBox_zhengzhou_house_quarter")
        sizePolicy2.setHeightForWidth(self.checkBox_zhengzhou_house_quarter.sizePolicy().hasHeightForWidth())
        self.checkBox_zhengzhou_house_quarter.setSizePolicy(sizePolicy2)

        self.horizontalLayout_6.addWidget(self.checkBox_zhengzhou_house_quarter, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_zhengzhou_house_qperiod = QComboBox(self.groupBox_2)
        self.comboBox_zhengzhou_house_qperiod.addItem("")
        self.comboBox_zhengzhou_house_qperiod.addItem("")
        self.comboBox_zhengzhou_house_qperiod.setObjectName(u"comboBox_zhengzhou_house_qperiod")
        sizePolicy2.setHeightForWidth(self.comboBox_zhengzhou_house_qperiod.sizePolicy().hasHeightForWidth())
        self.comboBox_zhengzhou_house_qperiod.setSizePolicy(sizePolicy2)
        self.comboBox_zhengzhou_house_qperiod.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid lightgrey;\n"
"    padding: 3px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.comboBox_zhengzhou_house_qperiod)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.checkBox_xinyang_road = QCheckBox(self.groupBox_2)
        self.checkBox_xinyang_road.setObjectName(u"checkBox_xinyang_road")
        sizePolicy2.setHeightForWidth(self.checkBox_xinyang_road.sizePolicy().hasHeightForWidth())
        self.checkBox_xinyang_road.setSizePolicy(sizePolicy2)

        self.horizontalLayout_9.addWidget(self.checkBox_xinyang_road, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_xinyang_road_period = QComboBox(self.groupBox_2)
        self.comboBox_xinyang_road_period.addItem("")
        self.comboBox_xinyang_road_period.setObjectName(u"comboBox_xinyang_road_period")
        sizePolicy2.setHeightForWidth(self.comboBox_xinyang_road_period.sizePolicy().hasHeightForWidth())
        self.comboBox_xinyang_road_period.setSizePolicy(sizePolicy2)
        self.comboBox_xinyang_road_period.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid lightgrey;\n"
"    padding: 3px;\n"
"}")

        self.horizontalLayout_9.addWidget(self.comboBox_xinyang_road_period, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.checkBox_zhengzhou_road = QCheckBox(self.groupBox_2)
        self.checkBox_zhengzhou_road.setObjectName(u"checkBox_zhengzhou_road")
        sizePolicy2.setHeightForWidth(self.checkBox_zhengzhou_road.sizePolicy().hasHeightForWidth())
        self.checkBox_zhengzhou_road.setSizePolicy(sizePolicy2)

        self.horizontalLayout_8.addWidget(self.checkBox_zhengzhou_road, 0, Qt.AlignmentFlag.AlignLeft)

        self.comboBox_zhengzhou_road_period = QComboBox(self.groupBox_2)
        self.comboBox_zhengzhou_road_period.addItem("")
        self.comboBox_zhengzhou_road_period.setObjectName(u"comboBox_zhengzhou_road_period")
        sizePolicy2.setHeightForWidth(self.comboBox_zhengzhou_road_period.sizePolicy().hasHeightForWidth())
        self.comboBox_zhengzhou_road_period.setSizePolicy(sizePolicy2)
        self.comboBox_zhengzhou_road_period.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid lightgrey;\n"
"    padding: 3px;\n"
"}")

        self.horizontalLayout_8.addWidget(self.comboBox_zhengzhou_road_period, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy1)
        self.groupBox_3.setMinimumSize(QSize(150, 0))
        self.groupBox_3.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    border: 1px solid gray; /* \u8bbe\u7f6e\u8fb9\u6846\u989c\u8272\u548c\u5bbd\u5ea6 */\n"
"    border-radius: 5px; /* \u8bbe\u7f6e\u8fb9\u6846\u5706\u89d2 */\n"
"    margin-top: 25px; /* \u8bbe\u7f6e\u6807\u9898\u4e0e\u5185\u5bb9\u7684\u95f4\u8ddd */\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin; /* \u6807\u9898\u4f4d\u7f6e */\n"
"    subcontrol-position: top center; /* \u6807\u9898\u5c45\u4e2d */\n"
"    padding: 0 3px; /* \u6807\u9898\u5185\u8fb9\u8ddd */   \n"
"}\n"
"")
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_personal_data = QCheckBox(self.groupBox_3)
        self.checkBox_personal_data.setObjectName(u"checkBox_personal_data")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(9)
        self.checkBox_personal_data.setFont(font2)

        self.verticalLayout_2.addWidget(self.checkBox_personal_data)

        self.pushButton_import = QPushButton(self.groupBox_3)
        self.pushButton_import.setObjectName(u"pushButton_import")
        sizePolicy2.setHeightForWidth(self.pushButton_import.sizePolicy().hasHeightForWidth())
        self.pushButton_import.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setKerning(True)
        self.pushButton_import.setFont(font3)
        self.pushButton_import.setStyleSheet(u"")
        icon = QIcon(QIcon.fromTheme(u"document-send"))
        self.pushButton_import.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_import)

        self.pushButton_export = QPushButton(self.groupBox_3)
        self.pushButton_export.setObjectName(u"pushButton_export")
        sizePolicy2.setHeightForWidth(self.pushButton_export.sizePolicy().hasHeightForWidth())
        self.pushButton_export.setSizePolicy(sizePolicy2)
        self.pushButton_export.setFont(font3)
        self.pushButton_export.setStyleSheet(u"")
        self.pushButton_export.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_export)

        self.pushButton_export_all = QPushButton(self.groupBox_3)
        self.pushButton_export_all.setObjectName(u"pushButton_export_all")
        self.pushButton_export_all.setStyleSheet(u"")
        self.pushButton_export_all.setIcon(icon)

        self.verticalLayout_2.addWidget(self.pushButton_export_all, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_4.addWidget(self.groupBox_3)

        self.horizontalSpacer_6 = QSpacerItem(162, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.lineEdit_period_keywords = QLineEdit(self.centralwidget)
        self.lineEdit_period_keywords.setObjectName(u"lineEdit_period_keywords")
        self.lineEdit_period_keywords.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.lineEdit_period_keywords.sizePolicy().hasHeightForWidth())
        self.lineEdit_period_keywords.setSizePolicy(sizePolicy2)
        self.lineEdit_period_keywords.setMinimumSize(QSize(200, 0))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setUnderline(False)
        self.lineEdit_period_keywords.setFont(font4)
        self.lineEdit_period_keywords.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #cccccc; /* \u8fb9\u6846\u989c\u8272 */\n"
"    border-radius: 5px; /* \u5706\u89d2\u534a\u5f84 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"    background: white; /* \u80cc\u666f\u989c\u8272 */\n"
"    selection-background-color: darkgray; /* \u9009\u4e2d\u6587\u672c\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #00aaff; /* \u805a\u7126\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"    background: #e6f7ff; /* \u805a\u7126\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.lineEdit_period_keywords.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit_period_keywords, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy2.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy2)
        self.lineEdit.setMinimumSize(QSize(200, 0))
        self.lineEdit.setMaximumSize(QSize(200, 30))
        font5 = QFont()
        font5.setPointSize(11)
        self.lineEdit.setFont(font5)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid #cccccc; /* \u8fb9\u6846\u989c\u8272 */\n"
"    border-radius: 5px; /* \u5706\u89d2\u534a\u5f84 */\n"
"    padding: 5px; /* \u5185\u8fb9\u8ddd */\n"
"    background: white; /* \u80cc\u666f\u989c\u8272 */\n"
"    selection-background-color: darkgray; /* \u9009\u4e2d\u6587\u672c\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #00aaff; /* \u805a\u7126\u65f6\u7684\u8fb9\u6846\u989c\u8272 */\n"
"    background: #e6f7ff; /* \u805a\u7126\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignLeft)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 30))
        self.pushButton.setSizeIncrement(QSize(0, 0))
        self.pushButton.setBaseSize(QSize(0, 0))
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1 Light"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setKerning(True)
        self.pushButton.setFont(font6)
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.pushButton.setStyleSheet(u"")
        icon1 = QIcon(QIcon.fromTheme(u"edit-find"))
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy3)
        self.tableView.setMaximumSize(QSize(16777215, 16777215))
        self.tableView.setStyleSheet(u"QMainWindow\n"
" {\n"
"                background-color: #87CEEB;  /* \u5929\u84dd\u8272\u80cc\u666f */\n"
"            }")

        self.verticalLayout_3.addWidget(self.tableView)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.label_total_records = QLabel(self.centralwidget)
        self.label_total_records.setObjectName(u"label_total_records")
        self.label_total_records.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_total_records)

        self.label_current_page = QLabel(self.centralwidget)
        self.label_current_page.setObjectName(u"label_current_page")

        self.horizontalLayout_7.addWidget(self.label_current_page)

        self.pushButton_next = QPushButton(self.centralwidget)
        self.pushButton_next.setObjectName(u"pushButton_next")
        self.pushButton_next.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pushButton_next)

        self.pushButton_previous = QPushButton(self.centralwidget)
        self.pushButton_previous.setObjectName(u"pushButton_previous")
        self.pushButton_previous.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pushButton_previous)

        self.pushButton_home = QPushButton(self.centralwidget)
        self.pushButton_home.setObjectName(u"pushButton_home")
        self.pushButton_home.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.pushButton_home)

        self.pushButton_price_catalog = QPushButton(self.centralwidget)
        self.pushButton_price_catalog.setObjectName(u"pushButton_price_catalog")

        self.horizontalLayout_7.addWidget(self.pushButton_price_catalog)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u4ef7", None))
        self.checkBox_gushi_house.setText(QCoreApplication.translate("MainWindow", u"\u56fa\u59cb\u623f\u5efa", None))
        self.comboBox_gushi_house_period.setItemText(0, QCoreApplication.translate("MainWindow", u"\u56fa\u59cb2024\u5e74\u7b2c2\u671f\u4fe1\u606f\u4ef7", None))
        self.comboBox_gushi_house_period.setItemText(1, QCoreApplication.translate("MainWindow", u"\u56fa\u59cb2024\u5e74\u7b2c1\u671f\u4fe1\u606f\u4ef7", None))

        self.checkBox_xinyang_house.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u9633\u623f\u5efa", None))
        self.comboBox_xinyang_house_period.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4fe1\u96332024\u5e74\u7b2c1\u671f\u4fe1\u606f\u4ef7", None))

        self.checkBox_zhengzhou_house_month.setText(QCoreApplication.translate("MainWindow", u"\u90d1\u5dde\u623f\u5efa\u6708\u4efd", None))
        self.comboBox_zhengzhou_house_mperiod.setItemText(0, QCoreApplication.translate("MainWindow", u"\u90d1\u5dde2024\u5e744\u6708\u4fe1\u606f\u4ef7", None))
        self.comboBox_zhengzhou_house_mperiod.setItemText(1, QCoreApplication.translate("MainWindow", u"\u90d1\u5dde2024\u5e743\u6708\u4fe1\u606f\u4ef7", None))

        self.checkBox_zhengzhou_house_quarter.setText(QCoreApplication.translate("MainWindow", u"\u90d1\u5dde\u623f\u5efa\u5b63\u5ea6", None))
        self.comboBox_zhengzhou_house_qperiod.setItemText(0, QCoreApplication.translate("MainWindow", u"\u90d1\u5dde2024\u5e741\u5b63\u5ea6\u4fe1\u606f\u4ef7", None))
        self.comboBox_zhengzhou_house_qperiod.setItemText(1, QCoreApplication.translate("MainWindow", u"\u90d1\u5dde2023\u5e744\u5b63\u5ea6\u4fe1\u606f\u4ef7", None))

        self.checkBox_xinyang_road.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u9633\u516c\u8def", None))
        self.comboBox_xinyang_road_period.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4fe1\u9633\u516c\u8def2024\u5e744\u6708\u4fe1\u606f\u4ef7", None))

        self.checkBox_zhengzhou_road.setText(QCoreApplication.translate("MainWindow", u"\u90d1\u5dde\u516c\u8def", None))
        self.comboBox_zhengzhou_road_period.setItemText(0, QCoreApplication.translate("MainWindow", u"\u90d1\u5dde\u516c\u8def2024\u5e744\u6708\u4fe1\u606f\u4ef7", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u4e13\u6709\u6570\u636e", None))
        self.checkBox_personal_data.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u6709\u6570\u636e", None))
        self.pushButton_import.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5bfc\u5165", None))
        self.pushButton_export.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6570\u636e\u5bfc\u51fa", None))
        self.pushButton_export_all.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u6570\u636e\u5bfc\u51fa", None))
        self.lineEdit_period_keywords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5730\u533a\u671f\u6570/\u7c7b\u522b", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0   \u89c4\u683c", None))
        self.pushButton.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.label_total_records.setText(QCoreApplication.translate("MainWindow", u"\u603b\u8bb0\u5f55\u6570: 0", None))
        self.label_current_page.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u9875: 1", None))
        self.pushButton_next.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u9875", None))
        self.pushButton_previous.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u9875", None))
        self.pushButton_home.setText(QCoreApplication.translate("MainWindow", u"\u9996\u9875", None))
        self.pushButton_price_catalog.setText(QCoreApplication.translate("MainWindow", u"\u4ef7\u683c\u76ee\u5f55", None))
    # retranslateUi

