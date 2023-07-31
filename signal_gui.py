from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont
from thread import CueGeneratorThread
import numpy as np
import joblib
import os

# plot_y = np.zeros((10))
# plot_x = np.arange(0,10,1)

class SignalWindow(QMainWindow):
    def __init__(self, iterations, trials, epoch_time, cue_class, name):
        super(SignalWindow, self).__init__()

        self.iterations = iterations
        self.trials = trials
        self.epoch_time = float(epoch_time)
        self.data_size = int(self.epoch_time/0.001)
        self.cue_class = cue_class
        self.name = name
        self.current_cue = None
        self.color = {
            'm': ['#eb3a34', '#c41b16', '#eb605b', '#d12d28', '#ba0d07', '#de8c8a', '#fa1007', '#c90d06'],
            'r': ['#06c9c6', '#076664', '#99f0ee'],
            'a': ['#8078bf', '#1f0bd4', '#6b5ced', '#524f75', '#4d42ad']
        }
        self.cue_color = self.color[cue_class]

        self.session_data = {
            'emg':np.empty((0,self.data_size)),
            'cue':list()
        }

        # Create a QLabel for the large section
        self.large_label = QLabel("Look here for the cues")
        self.large_label.setFont(QFont('Arial', 50))
        self.large_label.setAlignment(Qt.AlignCenter)

        # Create a Start button
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_clicked)

        # Set up the layout
        layout = QGridLayout()
        layout.addWidget(self.large_label, 0, 0, 2, 2)
        layout.addWidget(self.start_button, 3, 0, 1, 3)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_clicked(self):
        # Create the cue generator thread and connect the output signal to the output label
        self.thread = CueGeneratorThread(self.iterations, self.trials, self.epoch_time, self.cue_class, 'test')
        self.thread.output_signal.connect(self.update_output_label)
        self.thread.array.connect(self.update_data)

        # Start the thread
        self.thread.start()

    def update_output_label(self, output):
        # Update the output label with the current output
        random_color = np.random.choice(self.cue_color)
        self.large_label.setStyleSheet(f"color: {random_color};")
        self.large_label.setText(output)
        self.current_cue = output

    def update_data(self,array):
        self.session_data['emg'] = np.vstack((self.session_data['emg'],array.reshape(1,self.data_size)))
        self.session_data['cue'].append(self.current_cue)
        if self.current_cue=='End of sessions':
            current_dir = os.getcwd()
            # path = None
            print(self.session_data['emg'].shape, len(self.session_data['cue']))
            path = f'{current_dir}/dataset/{self.name}'
            try:
                count = len(os.listdir(path))+1
            except:
                os.mkdir(path)
                count = len(os.listdir(path))+1
            
            joblib.dump(self.session_data, f'{path}/{count}.sav')
