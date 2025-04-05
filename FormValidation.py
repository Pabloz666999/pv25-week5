import sys
from PyQt5.QtWidgets import *

class FormValidation(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.set_dark_mode()

    def setup_ui(self):
        self.name_label = QLabel('Name:')
        self.name_input = QLineEdit()

        self.email_label = QLabel('Email:')
        self.email_input = QLineEdit()

        self.age_label = QLabel('Age:')
        self.age_input = QLineEdit()

        self.phone_label = QLabel('Phone Number:')
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("+62")
        self.phone_input.setMaxLength(13)

        self.address_label = QLabel('Address:')
        self.address_input = QTextEdit()

        self.gender_label = QLabel('Gender:')
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(['Male', 'Female'])

        self.education_label = QLabel('Education:')
        self.education_combo = QComboBox()
        self.education_combo.addItems([
            'Elementary School', 'Junior High School', 'Senior High School',
            'Diploma', "Bachelor's Degree", "Master's Degree", 'Doctoral Degree'
        ])

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_profile)

        self.clear_button = QPushButton('Clear')
        self.clear_button.clicked.connect(self.clear_fields)

        self.creator_label = QLabel("Created by: M. Bayu Aji - NIM F1D02310144")

        form_layout = QFormLayout()
        form_layout.addRow(self.name_label, self.name_input)
        form_layout.addRow(self.email_label, self.email_input)
        form_layout.addRow(self.age_label, self.age_input)
        form_layout.addRow(self.phone_label, self.phone_input)
        form_layout.addRow(self.address_label, self.address_input)
        form_layout.addRow(self.gender_label, self.gender_combo)
        form_layout.addRow(self.education_label, self.education_combo)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.clear_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.creator_label)

        self.setLayout(main_layout)
        self.setWindowTitle('Form Validation')
        self.setGeometry(200, 200, 450, 300)

    def set_dark_mode(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #2d2d2d;
                color: white;
                font-family: Arial;
            }
            QLineEdit, QTextEdit, QComboBox {
                background-color: #3b3b3b;
                border: 1px solid #5a5a5a;
                color: white;
            }
            QPushButton {
                background-color: #5a5a5a;
                border: none;
                padding: 8px;
                color: white;
                border-radius: 5px;
            }
        """)

    def save_profile(self):
        name = self.name_input.text()
        email = self.email_input.text()
        age = self.age_input.text()
        phone = self.phone_input.text()
        address = self.address_input.toPlainText()
        gender = self.gender_combo.currentText()
        education = self.education_combo.currentText()

        if not all([name, email, age, phone, address]):
            self.show_error("All fields are required.")
            return

        if '@' not in email or not email.endswith('.com'):
            self.show_error("Email is not valid.")
            return

        if not age.isdigit():
            self.show_error("Age must be a number.")
            return

        if not phone.startswith("+62") or len(phone) != 13:
            self.show_error('Phone number must start with "+62" and have 13 digits.')
            return

        if any(char.isdigit() or not char.isalnum() and char != ' ' for char in name):
            self.show_error('Name cannot contain numbers or symbols.')
            return

        self.clear_fields()
        QMessageBox.information(self, 'Success', 'Profile saved successfully.')

    def show_error(self, message):
        QMessageBox.warning(self, 'Error', message)

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_combo.setCurrentIndex(0)
        self.education_combo.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FormValidation()
    window.show()
    sys.exit(app.exec_())
