from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys
import database
import os

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
            msg.error_message('Please enter password')
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
        
        self.d_birthday=self.findChild(QDateEdit, 'd_birthday')
        self.cb_gender=self.findChild(QComboBox, 'cb_gender')
        
        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.show_login)
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
            database.create_user(email, name, password)
            msg=Alert()
            msg.success_message('Registration successful')
            self.show_login()
            self.close()
            
    def show_login(self):
        self.login=Login()
        self.login.show()
        self.close()
        
class FieldItem(QWidget):
    def __init__(self, field_data, parent=None):
        super().__init__(parent)
        self.field_data = field_data
        uic.loadUi('ui/field_item.ui', self)
        self.setup_ui()
        
    def setup_ui(self):
        # Set field image
        if self.field_data['image_path']:
            pixmap = QPixmap(self.field_data['image_path'])
            scaled_pixmap = pixmap.scaled(280, 140, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)
        else:
            self.image_label.setStyleSheet("background-color: #f5f5f5;")
        
        # Set field name
        self.name_label.setText(self.field_data['name'])
        
        # Set field details with proper spacing
        details = [
            f"Location: {self.field_data['location']}",
            f"Capacity: {self.field_data['capacity']} players",
            f"Price: ${self.field_data['price']}/hour",
            f"Quality: {self.field_data['quality']}"
        ]
        
        self.details_label.setText("\n".join(details))
        self.details_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        
        # Set fixed size
        self.setFixedSize(280, 300)

class TimeSlot(QWidget):
    def __init__(self, time, status, parent=None):
        super().__init__(parent)
        uic.loadUi('ui/time_slot.ui', self)
        self.time = time
        self.status = status
        self.setup_ui()
        
    def setup_ui(self):
        self.time_label.setText(self.time)
        if self.status:
            self.status_label.setText("Booked")
            self.book_button.setText("Booked")
            self.book_button.setObjectName("booked_button")
            self.book_button.setEnabled(False)
        else:
            self.status_label.setText("Available")
            self.book_button.setText("Book")
            self.book_button.setObjectName("book_button")
            self.book_button.setEnabled(True)

class Home(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/mainwindow.ui', self)
        self.user_id = user_id
        self.user = database.find_user_by_id(user_id)
        
        # Navigation setup
        self.nav_home_btn = self.findChild(QPushButton,'nav_home_btn')
        self.nav_account_btn = self.findChild(QPushButton,'nav_account_btn')
        self.nav_new_btn = self.findChild(QPushButton,'nav_new_btn')
        self.stackedWidget = self.findChild(QStackedWidget,'stackedWidget')
        self.stackedWidget.setCurrentIndex(2)
        
        # Account page setup
        self.btn_avatar = self.findChild(QPushButton, "btn_avatar")
        self.btn_update_info = self.findChild(QPushButton, "btn_update_info")
        
        # Connect signals
        self.nav_home_btn.clicked.connect(lambda: self.navigateScreen(2))
        self.nav_account_btn.clicked.connect(lambda: self.navigateScreen(0))
        self.nav_new_btn.clicked.connect(lambda: self.navigateScreen(1))
        self.btn_avatar.clicked.connect(self.update_avatar)
        self.btn_update_info.clicked.connect(self.update_info)
        
        # Load user info and fields
        self.load_user_info()
        self.load_fields()

    def load_fields(self):
        container = self.page_2.findChild(QWidget, "widget")
        
        # Create grid layout if it doesn't exist
        if not container.layout():
            layout = QGridLayout()
            layout.setSpacing(10)  # Add 10px spacing between items
            layout.setContentsMargins(10, 10, 10, 10)  # Add margins around the grid
            container.setLayout(layout)
        else:
            layout = container.layout()
            # Clear existing widgets
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

        # Get all fields from database
        fields = database.get_all_fields()
        
        # Add fields to grid layout (3 columns)
        for i, field in enumerate(fields):
            field_item = FieldItem(field)
            field_item.setFixedSize(280, 270)  # Update fixed size to match UI
            field_item.view_button.clicked.connect(lambda checked, f=field: self.view_field(f))
            row = i // 3
            col = i % 3
            layout.addWidget(field_item, row, col)

    def view_field(self, field):
        # Navigate to page 5
        self.stackedWidget.setCurrentIndex(4)
        
        # Get the detail widget from page 5
        detail_widget = self.page_5.findChild(QWidget, "detail_widget")
        
        # Set field image
        field_image = detail_widget.findChild(QLabel, "field_image")
        if field.get('image_path') and os.path.exists(field['image_path']):
            pixmap = QPixmap(field['image_path'])
            scaled_pixmap = pixmap.scaled(800, 400, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            field_image.setPixmap(scaled_pixmap)
        else:
            field_image.setStyleSheet("background-color: #f5f5f5;")
            field_image.setText("No image available")
            field_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Set field name
        field_name = detail_widget.findChild(QLabel, "field_name")
        field_name.setText(field['name'])
        
        # Set field details
        details_widget = detail_widget.findChild(QWidget, "details_widget")
        details_layout = details_widget.findChild(QGridLayout, "details_layout")
        
        # Clear existing details
        while details_layout.count():
            item = details_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # Add field details in a grid
        details = [
            ("Location:", field['location']),
            ("Capacity:", f"{field['capacity']} players"),
            ("Price:", f"${field['price']}/hour"),
            ("Quality:", field['quality']),
            ("Description:", field.get('description', 'No description available'))
        ]
        
        for i, (label, value) in enumerate(details):
            label_widget = QLabel(label)
            label_widget.setStyleSheet("font-weight: bold; color: #FFFFFF;")
            value_widget = QLabel(value)
            details_layout.addWidget(label_widget, i, 0)
            details_layout.addWidget(value_widget, i, 1)
        
        # Set up schedule section
        date_picker = detail_widget.findChild(QDateEdit, "date_picker")
        date_picker.setDate(QDate.currentDate())
        date_picker.dateChanged.connect(lambda date: self.load_field_schedule(field['id'], date))
        
        # Get schedule content area
        schedule_content = detail_widget.findChild(QWidget, "schedule_content")
        schedule_layout = schedule_content.findChild(QVBoxLayout, "schedule_layout")
        
        # Set up back button
        back_button = detail_widget.findChild(QPushButton, "back_button")
        back_button.clicked.connect(lambda: self.navigateScreen(2))
        
        # Initial schedule load
        self.load_field_schedule(field['id'], date_picker.date())
        
    def load_field_schedule(self, field_id, date):
        # Get schedule content area
        detail_widget = self.page_5.findChild(QWidget, "detail_widget")
        schedule_content = detail_widget.findChild(QWidget, "schedule_content")
        schedule_layout = schedule_content.findChild(QVBoxLayout, "schedule_layout")
        
        # Clear existing schedule
        while schedule_layout.count():
            item = schedule_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
                
        # Initialize and get schedule for the date
        selected_date = date.toString("yyyy-MM-dd")
        database.initialize_field_schedule(field_id, selected_date)
        schedule = database.get_field_schedule(field_id, selected_date)
        
        # Add time slots
        for slot in schedule:
            time_slot = TimeSlot(slot['time'], slot['status'])
            if not slot['status']:  # If slot is available
                time_slot.book_button.clicked.connect(
                    lambda checked, t=slot['time']: self.book_field_slot(field_id, selected_date, t)
                )
            schedule_layout.addWidget(time_slot)
            
    def book_field_slot(self, field_id, date, time):
        if database.book_field(field_id, date, time, self.user_id):
            msg = Alert()
            msg.success_message(f"Successfully booked field for {time}")
            # Refresh the schedule
            detail_widget = self.page_5.findChild(QWidget, "detail_widget")
            date_picker = detail_widget.findChild(QDateEdit, "date_picker")
            self.load_field_schedule(field_id, date_picker.date())
        else:
            msg = Alert()
            msg.error_message("Failed to book field. Slot may no longer be available.")

    def navigateScreen(self, page:int):
        self.stackedWidget.setCurrentIndex(page)
        
    def load_user_info(self):
        self.txt_name=self.findChild(QLineEdit, 'txt_name')
        self.txt_email=self.findChild(QLineEdit, 'txt_email')
        self.btn_avatar=self.findChild(QPushButton, 'btn_avatar')
        self.d_birthday=self.findChild(QDateEdit, 'd_birthday')
        self.cb_gender=self.findChild(QComboBox, 'cb_gender')

        self.txt_name.setText(self.user["name"])
        self.txt_email.setText(self.user["email"])
        self.btn_avatar.setIcon(QIcon(self.user["avatar"]))
        self.d_birthday.setDate(QDate.fromString(self.user["birthday"], "dd/MM/yyyy"))
        self.cb_gender.setCurrentText(self.user["gender"])
        
    def update_avatar(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        if file:
            self.user["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            database.update_user_avatar(self.user_id, file)

    def update_info(self):
        name = self.txt_name.text()
        birthday = self.d_birthday.date().toString("dd/MM/yyyy")
        gender = self.cb_gender.currentText()
        database.update_user(self.user_id, name, birthday, gender)
        msg = Alert()
        msg.success_message("Update info success")
        self.load_user_info() 

if __name__=='__main__':
    app=QApplication(sys.argv)
    login=Login()
    login.show()
    sys.exit(app.exec())


