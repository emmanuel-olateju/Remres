import sys
import random
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from thread import CueGeneratorThread

class MainWindow(QMainWindow):
    def __init__(self, iterations, trials, epoch_time):
        super(MainWindow, self).__init__()

        self.iterations = iterations
        self.trials = trials
        self.epoch_time = epoch_time

        # Create a QLabel for the large section
        self.large_label = QLabel("Large Section")
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

        # Call the function to plot the data
        # self.plot_data()

    def start_clicked(self):
        # Create the cue generator thread and connect the output signal to the output label
        self.thread = CueGeneratorThread(self.iterations, self.trials, self.epoch_time, 'test')
        self.thread.output_signal.connect(self.update_output_label)
        self.thread.array.connect(self.update_figures)

        # Start the thread
        self.thread.start()

    def update_output_label(self, output):
        # Update the output label with the current output
        self.large_label.setText(output)

    def update_figures(self, readings):
        y = []
        datasize = int(self.epoch_time/0.001)

        for i in range(datasize):
            if not y:
                y = [0]
            else:
                y.append(y[-1] + 0.001)
                
        self.small_canvas1.figure.clear()
        self.small_canvas2.figure.clear()
        self.small_canvas3.figure.clear()

        # Create subplots and plot the data
        ax1 = self.small_canvas1.figure.add_subplot(111)
        ax1.scatter(readings, y, color='red')

        ax2 = self.small_canvas2.figure.add_subplot(111)
        ax2.scatter(readings, y, color='green')

        ax3 = self.small_canvas3.figure.add_subplot(111)
        ax3.scatter(readings, y, color='blue')

        # Refresh the canvases
        self.small_canvas1.draw()
        self.small_canvas2.draw()
        self.small_canvas3.draw()

        
    # def plot_data(self):
    #     # Generate some example data
    #     x1 = [1, 8, 9, 2, 4]
    #     x2 = [9, 4, 1, 5, 3]
    #     x3 = [2, 4, 7, 1, 5]

    #     y1 = [2, 4, 6, 8, 10]
    #     y2 = [1, 3, 5, 7, 9]
    #     y3 = [3, 6, 9, 12, 15]

    #     # Clear the previous plots
    #     self.small_canvas1.figure.clear()
    #     self.small_canvas2.figure.clear()
    #     self.small_canvas3.figure.clear()

    #     # Create subplots and plot the data
    #     ax1 = self.small_canvas1.figure.add_subplot(111)
    #     ax1.scatter(x1, y1, color='red')

    #     ax2 = self.small_canvas2.figure.add_subplot(111)
    #     ax2.scatter(x2, y2, color='green')

    #     ax3 = self.small_canvas3.figure.add_subplot(111)
    #     ax3.scatter(x3, y3, color='blue')

    #     # Refresh the canvases
    #     self.small_canvas1.draw()
    #     self.small_canvas2.draw()
    #     self.small_canvas3.draw()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
