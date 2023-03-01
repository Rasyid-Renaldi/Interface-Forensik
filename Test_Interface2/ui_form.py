from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFontComboBox,
                               QGroupBox, QLabel, QLineEdit, QListView,
                               QProgressBar, QPushButton, QRadioButton, QSizePolicy,
                               QWidget)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(991, 683)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 63, 20))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 20, 63, 20))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(210, 50, 581, 221))
        self.groupBox.setMouseTracking(False)
        self.groupBox.setFocusPolicy(Qt.StrongFocus)
        self.groupBox.setToolTipDuration(0)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 40, 91, 21))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 40, 341, 31))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 91, 21))
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(140, 90, 112, 26))
        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(140, 120, 112, 26))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 90, 91, 21))
        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(390, 90, 93, 26))
        self.checkBox_2 = QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(390, 120, 93, 26))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 160, 131, 21))
        self.OutputLocation = QFontComboBox(self.groupBox)
        self.OutputLocation.setObjectName(u"OutputLocation")
        self.OutputLocation.setGeometry(QRect(160, 160, 351, 31))
        self.OutputLocation.setAutoFillBackground(False)
        self.OutputLocation.setInputMethodHints(Qt.ImhUrlCharactersOnly)
        self.OutputLocation.setEditable(True)
        self.OutputLocation.setInsertPolicy(QComboBox.InsertAtBottom)
        self.OutputLocation.setDuplicatesEnabled(False)
        self.OutputLocation.setFrame(True)
        font = QFont()
        font.setFamilies([u"Location"])
        font.setKerning(True)
        self.OutputLocation.setCurrentFont(font)
        self.label_7 = QLabel(Widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(220, 300, 151, 31))
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(390, 300, 411, 41))
        self.progressBar.setValue(1)
        self.progressBar.setOrientation(Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QProgressBar.BottomToTop)
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(210, 360, 581, 211))
        self.listView = QListView(self.groupBox_2)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 30, 561, 171))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(730, 620, 83, 29))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(840, 620, 83, 29))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # !setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(
            QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"File", None))
        self.label_2.setText(
            QCoreApplication.translate("Widget", u"About", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "Widget", u"Destination File", None))
        self.label_3.setText(QCoreApplication.translate(
            "Widget", u"File Name     :", None))
        self.label_4.setText(QCoreApplication.translate(
            "Widget", u"Image Type   :", None))
        self.radioButton.setText(
            QCoreApplication.translate("Widget", u"Raw dd", None))
        self.radioButton_2.setText(
            QCoreApplication.translate("Widget", u"EnCase E01", None))
        self.label_5.setText(QCoreApplication.translate(
            "Widget", u"Storage      :", None))
        self.checkBox.setText(QCoreApplication.translate(
            "Widget", u"Internal", None))
        self.checkBox_2.setText(
            QCoreApplication.translate("Widget", u"Eksternal", None))
        self.label_6.setText(QCoreApplication.translate(
            "Widget", u"Output Location    :", None))
        self.OutputLocation.setCurrentText(
            QCoreApplication.translate("Widget", u"Location", None))
        self.label_7.setText(QCoreApplication.translate(
            "Widget", u"Acquisition Progress   :", None))
        self.progressBar.setFormat(
            QCoreApplication.translate("Widget", u"%p%", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Widget", u"Details", None))
        self.pushButton.setText(
            QCoreApplication.translate("Widget", u"Back", None))
        self.pushButton_2.setText(
            QCoreApplication.translate("Widget", u"Extract", None))
    # !retranslateUi
