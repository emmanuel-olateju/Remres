import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from settings_gui import SettingsWindow
from PyQt5.QtGui import QIntValidator

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle('User Information')

        # Create labels
        self.name_label = QLabel('Name:', self)
        self.age_label = QLabel('Age:', self)
        self.affected_part_label = QLabel('Affected Part:', self)
        self.residual_capability_label = QLabel('Residual Sensory Capability:', self)
        self.gender_label = QLabel('Gender:', self)

        # Create input fields
        self.name_input = QLineEdit(self)
        self.age_input = QLineEdit(self)
        self.age_input.setValidator(QIntValidator(1, 99))  # Only accept integers
        self.affected_part_input = QLineEdit(self)
        self.residual_capability_input = QComboBox(self)
        self.residual_capability_input.addItems([str(i) for i in range(11)])  # Dropdown with options 0-10
        self.gender_input = QComboBox(self)
        self.gender_input.addItems(['Male', 'Female'])  # Dropdown with options Male and Female

        # Create submit button
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submit_clicked)

        # Set layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)
        layout.addWidget(self.affected_part_label)
        layout.addWidget(self.affected_part_input)
        layout.addWidget(self.residual_capability_label)
        layout.addWidget(self.residual_capability_input)
        layout.addWidget(self.gender_label)
        layout.addWidget(self.gender_input)
        layout.addWidget(self.submit_button)

    def submit_clicked(self):
        # Get the entered information
        name = self.name_input.text()
        age = self.age_input.text()
        affected_part = self.affected_part_input.text()
        residual_capability = self.residual_capability_input.currentText()
        gender = self.gender_input.currentText()

        # Write the information to a file
        with open('user_information.txt', 'w') as file:
            file.write(f'Name: {name}\n')
            file.write(f'Age: {age}\n')
            file.write(f'Affected Part: {affected_part}\n')
            file.write(f'Residual Sensory Capability: {residual_capability}\n')
            file.write(f'Gender: {gender}\n')
        
        # Close window
        self.close()

        # Open the new window
        self.new_window = SettingsWindow()
        self.new_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
