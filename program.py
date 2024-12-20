from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QMessageBox, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6 import uic
import sys
import database

class Alert(QMessageBox):
    def error_message(self, message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle('Error')
        self.exec()
        
    def success_message(self, message):
        self.setIcon(QMessageBox.Icon.Information)
        self.setText(message)
        self.setWindowTitle('Success')
        self.exec()

class Login(QMainWindow):
    def __init__(self):
        super(). __init__()
        uic.loadUi('ui/login.ui', self)
        
        self.email_input=self.findChild(QLineEdit, 'txt_email')
        self.password_input=self.findChild(QLineEdit, 'txt_password')
        self.btn_login=self.findChild(QPushButton,'btn_login')
        self.btn_register=self.findChild(QPushButton, 'btn_register')
        self.btn_eye=self.findChild(QPushButton, 'btn_eye')
        
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_eye.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_eye))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))

        
    def login(self):
        email=self.email_input.text()
        password=self.password_input.text()
        
        if email=='':
            msg=Alert()
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        
        if password=='':
            msg=Alert()
            msg.error_message('Pleas enter password')
            self.password_input.setFocus()
            return
        
        user=database.find_user_by_email_and_password(email, password)
        if user:
            msg=Alert()
            msg.success_message('Login successful')
            self.show_main(user["id"])
        else:
            msg=Alert()
            msg.error_message('Invalid email or password')
            
    def show_register(self):
        self.register=Register()
        self.register.show()
        self.close()
        
    def show_main(self, user_id):
        self.home = Home(user_id)
        self.home.show()
        self.close()
            
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/signup.ui', self)
        
        self.email_input=self.findChild(QLineEdit, 'txt_email')
        self.name_input=self.findChild(QLineEdit, 'txt_name')
        self.password_input=self.findChild(QLineEdit, 'txt_password')
        self.confirm_password_input=self.findChild(QLineEdit, 'txt_confirm_password')
        
    
        self.btn_login=self.findChild(QPushButton, 'btn_login')
        self.btn_register=self.findChild(QPushButton, 'btn_register')
        self.btn_eye1=self.findChild(QPushButton, 'btn_eye1')
        self.btn_eye2=self.findChild(QPushButton, 'btn_eye2')
        
        self.btn_login.clicked.connect(self.register)
        self.btn_register.clicked.connect(self.show_login)
        self.btn_eye1.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_eye1))
        self.btn_eye2.clicked.connect(lambda: self.hiddenOrShow(self.confirm_password_input, self.btn_eye2))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))

    def register(self):
        email=self.email_input.text()
        name=self.name_input.text()
        password=self.password_input.text()
        confirm_password=self.confirm_password_input.text()
        
        if email=='':
            msg=Alert()
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        
        if password=='':
            msg=Alert()
            msg.error_message('Pleas enter password')
            self.password_input.setFocus()
            return
        
        if confirm_password=='':
            msg=Alert()
            msg.error_message('Please enter confirm password')
            self.confirm_password_input.setFocus
            return
        
        if password!=confirm_password:
            msg=Alert()
            msg.error_message('Password and confirm password does not match')
            self.confirm_password_input.setFocus()
            return
        
        user=database.find_user_by_email(email)
        if user:
            msg=Alert()
            msg.error_message('Email already exists')
        else:
            database.create_user(email,password)
            msg=Alert()
            msg.success_message('Registration successful')
            self.show_login()
            self.close()
            
    def show_login(self):
        self.login=Login()
        self.login.show()
        self.close()
        
class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.user_id = user_id
            
if __name__=='__main__':
    app=QApplication(sys.argv)
    login=Login()
    login.show()
    sys.exit(app.exec())


