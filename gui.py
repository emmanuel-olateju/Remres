import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class CueGeneratorThread(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self, iterations, trials, epoch_time):
        super().__init__()
        self.iterations = iterations
        self.trials = trials
        self.epoch_time = epoch_time

    def run(self):
        for i in range(self.iterations):
            output = cue_generator(self.trials)
            self.output_signal.emit(output)
            time.sleep(self.epoch_time)
            self.output_signal.emit('')

def cue_generator(trials):
    # Your implementation of the cue generator function goes here
    # This is just an example implementation that returns a string with the number of trials
    return f"{trials} trials generated"

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the widgets
        self.iterations_label = QLabel('Number of session iterations:', self)
        self.trials_label = QLabel('Trials per class:', self)
        self.epoch_time_label = QLabel('Epoch time (seconds):', self)
        self.iterations_input = QLineEdit(self)
        self.trials_input = QLineEdit(self)
        self.epoch_time_input = QLineEdit(self)
        self.generate_button = QPushButton('Generate', self)
        self.output_label = QLabel(self)

        # Create the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.iterations_label)
        vbox.addWidget(self.iterations_input)
        vbox.addWidget(self.trials_label)
        vbox.addWidget(self.trials_input)
        vbox.addWidget(self.epoch_time_label)
        vbox.addWidget(self.epoch_time_input)
        vbox.addWidget(self.generate_button)
        vbox.addWidget(self.output_label)
        self.setLayout(vbox)

        # Connect the generate button to the generate function
        self.generate_button.clicked.connect(self.generate)

    def generate(self):
        # Get the inputs from the user
        iterations = int(self.iterations_input.text())
        trials = int(self.trials_input.text())
        epoch_time = int(self.epoch_time_input.text())

        # Create the cue generator thread and connect the output signal to the output label
        self.thread = CueGeneratorThread(iterations, trials, epoch_time)
        self.thread.output_signal.connect(self.update_output_label)

        # Start the thread
        self.thread.start()

    def update_output_label(self, output):
        # Update the output label with the current output
        current_text = self.output_label.text()
        if current_text == '':
            self.output_label.setText(output)
        else:
            self.output_label.setText(f"{current_text}\n{output}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
