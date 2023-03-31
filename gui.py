import sys
import time
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from gui_cue_generator import cue_generator
from .gui_emg_object import emg_signal

class CueGeneratorThread(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self, iterations, trials, epoch_time):
        super().__init__()
        self.iterations = iterations
        self.trials = trials
        self.epoch_time = epoch_time
        self.dataset = {}
        data_size = int(self.epoch_time/0.001)
        self.shape = np.empty((0, data_size))
        self.emg = emg_signal(26, self.epoch_time)  

    def run(self):
        DAQ = 0
        self.output_signal.emit('Start of Sessions')
        time.sleep(2)

        while DAQ != self.iterations:
            DAQ += 1
            cue_class, cues, useTime = cue_generator(self.trials)
            self.dataset[cue_class] = {}
            self.output_signal.emit(f'Cue Class- {cue_class}')
            time.sleep(2)

            for cue in cues:
                readings = self.emg.__read()
                self.dataset[cue_class][cue] = np.vstack((self.shape, readings))     
                self.output_signal.emit(cue)
                time.sleep(self.epoch_time)
        self.output_signal.emit('End of sessions')
        print(self.dataset)
        

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
        self.output_label.setText(output)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
