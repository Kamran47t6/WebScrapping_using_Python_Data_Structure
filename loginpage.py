from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
from loginpage import Ui_Form  # Import the generated UI class

class YourApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        # Connect the button click event to open LinkedIn profile
        self.ui.linkedinbtn.clicked.connect(self.openLinkedInProfile)
        self.ui.githubbtn.clicked.connect(self.openGitHubProfile)
        self.ui.youtubebtn.clicked.connect(self.openYoutubeChannel)
        self.ui.instabtnbtn.clicked.connect(self.openInstaProfile)

    def openLinkedInProfile(self):
        # Replace 'your_linkedin_profile_url' with your actual LinkedIn profile URL
        url = QUrl("https://www.linkedin.com/in/muhammad-kamran-4a9539257?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
        QDesktopServices.openUrl(url)
    def openGitHubProfile(self):
        # Replace 'your_linkedin_profile_url' with your actual LinkedIn profile URL
        url = QUrl("https://github.com/Kamran47t6")
        QDesktopServices.openUrl(url)
    def openYoutubeChannel(self):
        # Replace 'your_linkedin_profile_url' with your actual LinkedIn profile URL
        url = QUrl("https://www.youtube.com/channel/UC1f4GrK9_ZRRjSyjZ0rao6A")
        QDesktopServices.openUrl(url)
    def openInstaProfile(self):
        # Replace 'your_linkedin_profile_url' with your actual LinkedIn profile URL
        url = QUrl("https://www.linkedin.com/in/muhammad-kamran-4a9539257?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
        QDesktopServices.openUrl(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YourApp()
    window.show()
    sys.exit(app.exec_())


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(441, 479)
        Form.setStyleSheet("QPushButton#pushButton(qlineargradient{\n"
"spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color:rgba(255,255,255,210);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover(qlineargradient{\n"
"spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(34, 47, 78, 219), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(105,118,132,200)\n"
"}\n"
"QPushButton#pushButton_2{\n"
"background-color:rgba(0,0,0,0);\n"
"color:rgba(85,98,112,255);\n"
"\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"color:rgba(155,168,182,220);\n"
"\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(105,118,132,200)\n"
"}")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 370, 480))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(80, 70, 281, 400))
        self.label.setStyleSheet("border-image: url(:/images/LoginUi/loginimg2.jpg);\n"
"border-radius:70px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 301, 400))
        self.label_2.setStyleSheet("border-image: url(:/images/LoginUi/loginimg2.jpg);\n"
"border-radius:70px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(110, 110, 241, 331))
        self.label_3.setStyleSheet("background-color:rgba(0,0,0,100);\n"
"border-radius:15px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(190, 130, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(225,225,225,210);\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 190, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 260, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:rgba(255,255,255,230);\n"
"padding-bottom:7px;\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 320, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(140, 370, 141, 16))
        self.label_5.setStyleSheet("color:rgba(255,255,255,140);\n"
"")
        self.label_5.setObjectName("label_5")
        self.linkedinbtn = QtWidgets.QPushButton(self.widget)
        self.linkedinbtn.setGeometry(QtCore.QRect(190, 400, 21, 21))
        self.linkedinbtn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        self.linkedinbtn.setFont(font)
        self.linkedinbtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.linkedinbtn.setStyleSheet("background-image: url(:/images/LoginUi/resize-16974932511908711249174857.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.linkedinbtn.setText("")
        self.linkedinbtn.setObjectName("linkedinbtn")
        self.githubbtn = QtWidgets.QPushButton(self.widget)
        self.githubbtn.setGeometry(QtCore.QRect(220, 400, 21, 21))
        self.githubbtn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        self.githubbtn.setFont(font)
        self.githubbtn.setStyleSheet("background-image: url(:/images/LoginUi/resize-169749355418085788625231.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;")
        self.githubbtn.setText("")
        self.githubbtn.setObjectName("githubbtn")
        self.youtubebtn = QtWidgets.QPushButton(self.widget)
        self.youtubebtn.setGeometry(QtCore.QRect(250, 400, 21, 21))
        self.youtubebtn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        self.youtubebtn.setFont(font)
        self.youtubebtn.setStyleSheet("background-image: url(:/images/LoginUi/resize-16974936031207048446Youtubelogo.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;")
        self.youtubebtn.setText("")
        self.youtubebtn.setObjectName("youtubebtn")
        self.instabtn = QtWidgets.QPushButton(self.widget)
        self.instabtn.setGeometry(QtCore.QRect(280, 400, 21, 21))
        self.instabtn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiCondensed")
        self.instabtn.setFont(font)
        self.instabtn.setStyleSheet("background-image: url(:/images/LoginUi/resize-1697493625277788002pngtreeinstagramiconpngimage6315974.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;")
        self.instabtn.setText("")
        self.instabtn.setObjectName("instabtn")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(140, 400, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:rgba(255,255,255,140);\n"
"")
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))
        self.label_5.setText(_translate("Form", "Forget UserName or Password ?"))
        self.label_6.setText(_translate("Form", "Follow Us"))
import res_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
