import time
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from gui_cue_generator import cue_generator
from emg_object import emg_signal

class CueGeneratorThread(QThread):
    output_signal = pyqtSignal(str)
    array = pyqtSignal(np.ndarray)

    def __init__(self, iterations, trials, epoch_time, cue_class, file_name=' '):
        super().__init__()
        self.iterations = int(iterations)
        self.trials = int(trials)
        self.epoch_time = float(epoch_time)
        self.cue_class = cue_class
        self.dataset = {}
        self.data_size = int(self.epoch_time/0.001)
        self.shape = np.empty((0, self.data_size))
        self.emg = emg_signal('COM7', self.epoch_time, 'test') 

    def run(self):
        DAQ = 0

        while DAQ != self.iterations:
            DAQ += 1
            cue_class, cues, useTime = cue_generator(self.trials, self.cue_class)
            self.dataset[cue_class] = {}

            for cue in cues+['End of sessions']:   
                count = 1
                self.output_signal.emit(cue)
                print(cue)
                epoch=list()
                for  i in range(self.data_size+10):
                    self.readings = self.emg.read() 
                    print(self.readings)
                    if count > 10:
                        epoch.append(self.readings)
                    count += 1
                self.array.emit(np.array(epoch))
        self.output_signal.emit('End of sessions')
