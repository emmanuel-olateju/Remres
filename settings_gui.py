import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox
from PyQt5.QtGui import QFont
from signal_gui import SignalWindow
        

class SettingsWindow(QWidget):
    def __init__(self, name):
        super().__init__()

        # Create the widgets
        self.name = name
        self.iterations_label = QLabel('Number of session iterations:', self)
        self.trials_label = QLabel('Trials per class:', self)
        self.epoch_time_label = QLabel('Epoch time (seconds):', self)
        self.cue_class_label = QLabel('Cue class choice:', self)
        self.iterations_input = QLineEdit(self)
        self.trials_input = QLineEdit(self)
        self.epoch_time_input = QLineEdit(self)
        self.cue_class_input = QComboBox(self)
        self.cue_class_input.addItems(['m', 'r', 'a'])
        self.generate_button = QPushButton('Generate', self)
        self.output_label = QLabel(self)

        # Style Labels
        self.iterations_label.setFont(QFont('Arial', 10))
        self.trials_label.setFont(QFont('Arial', 10))
        self.epoch_time_label.setFont(QFont('Arial', 10))
        self.cue_class_label.setFont(QFont('Arial', 10))

        # Create the layout
        vbox = QVBoxLayout(self)
        vbox.addWidget(self.iterations_label)
        vbox.addWidget(self.iterations_input)
        vbox.addWidget(self.trials_label)
        vbox.addWidget(self.trials_input)
        vbox.addWidget(self.epoch_time_label)
        vbox.addWidget(self.epoch_time_input)
        vbox.addWidget(self.cue_class_label)
        vbox.addWidget(self.cue_class_input)
        vbox.addWidget(self.generate_button)
        vbox.addWidget(self.output_label)

        # Connect the generate button to the generate function
        self.generate_button.clicked.connect(self.generate)

    def generate(self):
        iterations = self.iterations_input.text()
        trials = self.trials_input.text()
        epoch_time = self.epoch_time_input.text()
        cue_class = self.cue_class_input.currentText()

        self.close()
        self.new_window = SignalWindow(iterations, trials, epoch_time, cue_class, self.name)
        self.new_window.show()
