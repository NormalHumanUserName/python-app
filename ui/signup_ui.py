# Form implementation generated from reading ui file '/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/TriKhiem/python-app/ui/signup.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1405, 768)
        Form.setStyleSheet("")
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setGeometry(QtCore.QRect(110, 610, 241, 41))
        self.label_6.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=Form)
        self.label_7.setGeometry(QtCore.QRect(110, 80, 471, 91))
        self.label_7.setStyleSheet("font: 700 30pt \"Rockwell\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setGeometry(QtCore.QRect(190, 260, 191, 51))
        self.label_8.setStyleSheet("font: 16pt \"Segoe UI\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=Form)
        self.label_9.setGeometry(QtCore.QRect(190, 380, 171, 31))
        self.label_9.setStyleSheet("font: 16pt \"Segoe UI\";")
        self.label_9.setObjectName("label_9")
        self.txt_password = QtWidgets.QLineEdit(parent=Form)
        self.txt_password.setGeometry(QtCore.QRect(190, 420, 281, 61))
        self.txt_password.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"border-radius:15px")
        self.txt_password.setText("")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_password.setObjectName("txt_password")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(50, 30, 171, 51))
        self.label_3.setStyleSheet("font: 15pt \"Showcard Gothic\";")
        self.label_3.setObjectName("label_3")
        self.txt_email = QtWidgets.QLineEdit(parent=Form)
        self.txt_email.setGeometry(QtCore.QRect(190, 310, 281, 61))
        self.txt_email.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"border-radius:15px")
        self.txt_email.setText("")
        self.txt_email.setObjectName("txt_email")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(700, 0, 711, 771))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/TriKhiem/python-app/ui/../img/download.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(940, 260, 251, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/TriKhiem/python-app/ui/../../../../Downloads/f78441300cf50b8f8a2cf9d44e2225e9.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(parent=Form)
        self.label_10.setGeometry(QtCore.QRect(190, 490, 221, 31))
        self.label_10.setStyleSheet("font: 16pt \"Segoe UI\";")
        self.label_10.setObjectName("label_10")
        self.txt_confirm_password = QtWidgets.QLineEdit(parent=Form)
        self.txt_confirm_password.setGeometry(QtCore.QRect(190, 530, 281, 61))
        self.txt_confirm_password.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"border-radius:15px")
        self.txt_confirm_password.setText("")
        self.txt_confirm_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.txt_confirm_password.setObjectName("txt_confirm_password")
        self.btn_eye1 = QtWidgets.QPushButton(parent=Form)
        self.btn_eye1.setGeometry(QtCore.QRect(430, 440, 31, 29))
        self.btn_eye1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/pinxun/Documents/MindX/PTA/PTA07/FINAL PROJECT/TriKhiem/python-app/ui/../img/eye-slash-solid.svg"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_eye1.setIcon(icon)
        self.btn_eye1.setObjectName("btn_eye1")
        self.btn_eye2 = QtWidgets.QPushButton(parent=Form)
        self.btn_eye2.setGeometry(QtCore.QRect(430, 550, 31, 29))
        self.btn_eye2.setText("")
        self.btn_eye2.setIcon(icon)
        self.btn_eye2.setObjectName("btn_eye2")
        self.btn_login = QtWidgets.QPushButton(parent=Form)
        self.btn_login.setGeometry(QtCore.QRect(350, 610, 231, 51))
        self.btn_login.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 80px;\n"
"font-size: 18px;\n"
"text-align: center;\n"
"    ")
        self.btn_login.setObjectName("btn_login")
        self.btn_register = QtWidgets.QPushButton(parent=Form)
        self.btn_register.setGeometry(QtCore.QRect(190, 680, 281, 61))
        self.btn_register.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"border-radius: 8px;\n"
"padding: 80px;\n"
"font-size: 18px;\n"
"text-align: center;\n"
"    ")
        self.btn_register.setObjectName("btn_register")
        self.txt_name = QtWidgets.QLineEdit(parent=Form)
        self.txt_name.setGeometry(QtCore.QRect(190, 210, 281, 61))
        self.txt_name.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"border-radius:15px")
        self.txt_name.setText("")
        self.txt_name.setObjectName("txt_name")
        self.label_11 = QtWidgets.QLabel(parent=Form)
        self.label_11.setGeometry(QtCore.QRect(190, 160, 191, 51))
        self.label_11.setStyleSheet("font: 16pt \"Segoe UI\";")
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Already have an account?"))
        self.label_7.setText(_translate("Form", "Sign up to Football!"))
        self.label_8.setText(_translate("Form", "Email"))
        self.label_9.setText(_translate("Form", "Password"))
        self.txt_password.setPlaceholderText(_translate("Form", "Please enter Password"))
        self.label_3.setText(_translate("Form", "PitchPoint"))
        self.txt_email.setPlaceholderText(_translate("Form", "Please enter Email"))
        self.label_10.setText(_translate("Form", "Confirm Password"))
        self.txt_confirm_password.setPlaceholderText(_translate("Form", "Please enter Password"))
        self.btn_login.setText(_translate("Form", "Login"))
        self.btn_register.setText(_translate("Form", "Sign up"))
        self.txt_name.setPlaceholderText(_translate("Form", "Please enter Username"))
        self.label_11.setText(_translate("Form", "Username"))
