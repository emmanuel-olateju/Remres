import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from thread import CueGeneratorThread
import numpy as np

plot_y = np.zeros((300))
plot_x = np.arange(0,300,1)

class SignalWindow(QMainWindow):
    def __init__(self, iterations, trials, epoch_time, cue_class):
        super(SignalWindow, self).__init__()

        self.iterations = iterations
        self.trials = trials
        self.epoch_time = float(epoch_time)
        self.cue_class = cue_class

        # Create a QLabel for the large section
        self.large_label = QLabel("Look here for the cues")
        self.large_label.setAlignment(Qt.AlignCenter)

        # Create FigureCanvases for the small plots
        self.small_canvas1 = FigureCanvas(plt.figure())
        self.small_canvas2 = FigureCanvas(plt.figure())
        self.small_canvas3 = FigureCanvas(plt.figure())

        # Create a Start button
        self.start_button = QPushButton('Start')
        self.start_button.clicked.connect(self.start_clicked)

        # Set up the layout
        layout = QGridLayout()
        layout.addWidget(self.large_label, 0, 0, 2, 2)
        layout.addWidget(self.small_canvas1, 0, 2)
        layout.addWidget(self.small_canvas2, 1, 2)
        layout.addWidget(self.small_canvas3, 2, 2)
        layout.addWidget(self.start_button, 3, 0, 1, 3)

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def start_clicked(self):
        # Create the cue generator thread and connect the output signal to the output label
        self.thread = CueGeneratorThread(self.iterations, self.trials, self.epoch_time, self.cue_class, 'test')
        self.thread.output_signal.connect(self.update_output_label)
        self.thread.array.connect(self.update_figures)

        # Start the thread
        self.thread.start()

    def update_output_label(self, output):
        # Update the output label with the current output
        self.large_label.setText(output)

    def update_figures(self, readings):
        plot_y[:-1]=plot_y[1:]
        plot_y[-1] = readings
        print(plot_y)
        
        datasize = int(self.epoch_time/0.001)

        # for i in range(datasize):
        #     if not plot_y:
        #         plot_y = [0]
        #     else:
        #         y.append(y[-1] + 0.001)
                
        self.small_canvas1.figure.clear()
        # ax1 = self.small_canvas1.figure.add_subplot(111)
        # ax1.plot(plot_x,plot_y)
        # self.small_canvas2.figure.clear()
        # self.small_canvas3.figure.clear()

        # # Create subplots and plot the data
        ax1 = self.small_canvas1.figure.add_subplot(111)
        ax1.plot(plot_x, plot_y, color='red')
        # ax1.set_facecolor('none')
        ax1.set_title('Raw EMG Signal')

        # ax2 = self.small_canvas2.figure.add_subplot(111)
        # ax2.scatter(plot_x, plot_y, color='green', alpha=0.7)
        # ax2.set_facecolor('none')
        # ax2.set_title('Filtered EMG Signal')

        # ax3 = self.small_canvas3.figure.add_subplot(111)
        # ax3.scatter(plot_x, plot_y, color='blue', alpha=0.7)
        # ax3.set_facecolor('none')
        # ax3.set_title('Analysis')

        # # Refresh the canvases
        self.small_canvas1.draw()
        # self.small_canvas2.draw()
        # self.small_canvas3.draw()
