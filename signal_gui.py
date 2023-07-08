from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from thread import CueGeneratorThread

class SignalWindow(QWidget):
    def __init__(self, iterations, trials, epoch_time):
        self.iterations = iterations
        self.trials = trials
        self.epoch_time = epoch_time
        super().__init__()

        # Set window title
        self.setWindowTitle('Signals Screen')

        # Create layouts
        main_layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()
        bottom_layout = QHBoxLayout()

        # Create labels for each part
        self.large_label = QLabel('Large Part', self)
        self.small_label1 = QLabel('Small Part 1', self)
        self.small_label2 = QLabel('Small Part 2', self)
        self.small_label3 = QLabel('Small Part 3', self)

        # Set the large part label to stretch horizontally
        self.large_label.setMinimumWidth(300)
        self.large_label.setAlignment(Qt.AlignCenter)

        # Add labels to layouts
        top_layout.addWidget(self.large_label)
        bottom_layout.addWidget(self.small_label1)
        bottom_layout.addWidget(self.small_label2)
        bottom_layout.addWidget(self.small_label3)

        # Create start button
        start_button = QPushButton('Start', self)
        start_button.clicked.connect(self.start_clicked)

        # Add layouts and start button to the main layout
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)
        main_layout.addWidget(start_button, alignment=Qt.AlignCenter)

    def start_clicked(self):
        # Create the cue generator thread and connect the output signal to the output label
        self.thread = CueGeneratorThread(self.iterations, self.trials, self.epoch_time, 'test')
        self.thread.output_signal.connect(self.update_output_label)

        # Start the thread
        self.thread.start()

    def update_output_label(self, output):
        # Update the output label with the current output
        self.large_label.setText(output)


# app = QApplication([])
# window = MainWindow()
# window.show()
# app.exec_()
