from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QColumnView, QGroupBox, QLabel,
                               QListView, QPushButton, QSizePolicy, QWidget)


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1064, 600)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(240, 70, 191, 41))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 63, 20))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 10, 63, 20))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(460, 70, 191, 41))
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(680, 70, 191, 41))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(40, 150, 451, 191))
        self.devicesView = QColumnView(self.groupBox)
        self.devicesView.setObjectName(u"devicesView")
        self.devicesView.setGeometry(QRect(10, 30, 431, 151))
        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(570, 150, 441, 191))
        self.detailsView = QListView(self.groupBox_2)
        self.detailsView.setObjectName(u"detailsView")
        self.detailsView.setGeometry(QRect(10, 30, 411, 151))
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(400, 380, 83, 29))
        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(500, 380, 83, 29))
        self.pushButton_6 = QPushButton(Widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(610, 380, 83, 29))
        self.pushButton_7 = QPushButton(Widget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(750, 510, 83, 29))
        self.pushButton_8 = QPushButton(Widget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(860, 510, 83, 29))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # !setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(
            QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate(
            "Widget", u"ADB Reboot-Bootloader", None))
        self.label.setText(QCoreApplication.translate("Widget", u"File", None))
        self.label_2.setText(
            QCoreApplication.translate("Widget", u"About", None))
        self.pushButton_2.setText(QCoreApplication.translate(
            "Widget", u"ADB Reboot-Download", None))
        self.pushButton_3.setText(QCoreApplication.translate(
            "Widget", u"ADB Reboot-Recovery", None))
        self.groupBox.setTitle(QCoreApplication.translate(
            "Widget", u"Detect Devices", None))
        self.groupBox_2.setTitle(
            QCoreApplication.translate("Widget", u"Details", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("Widget", u"Scan", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("Widget", u"Check", None))
        self.pushButton_6.setText(
            QCoreApplication.translate("Widget", u"Connect", None))
        self.pushButton_7.setText(
            QCoreApplication.translate("Widget", u"Exit", None))
        self.pushButton_8.setText(
            QCoreApplication.translate("Widget", u"Next", None))
    # !retranslateUi
