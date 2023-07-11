import time
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from matplotlib.figure import Figure
from gui_cue_generator import cue_generator
from gui_emg_object import emg_signal

class CueGeneratorThread(QThread):
    output_signal = pyqtSignal(str)
    array = pyqtSignal(np.ndarray)

    def __init__(self, iterations, trials, epoch_time, file_name=' '):
        super().__init__()
        self.iterations = int(iterations)
        self.trials = int(trials)
        self.epoch_time = float(epoch_time)
        self.dataset = {}
        self.data_size = int(self.epoch_time/0.001)
        self.shape = np.empty((0, self.data_size))
        self.emg = emg_signal(26, self.epoch_time) 

        # if file_name != ' ':
        #     print('file use')
        #     self.file = open(file_name+'.csv','w')
        # else:
        #     self.file = None 

    def run(self):
        DAQ = 0
        self.output_signal.emit('Start of Sessions')
        # time.sleep(2)

        while DAQ != self.iterations:
            DAQ += 1
            cue_class, cues, useTime = cue_generator(self.trials)
            self.dataset[cue_class] = {}

            for cue in cues:   
                # self.output_signal.emit(cue)
                self.readings = self.emg.continuous_read() 
                self.output_signal.emit(cue)
                self.array.emit(self.readings) 
                # time.sleep(self.epoch_time)
                
                try:
                    if not self.dataset[cue_class].get(cue, None):
                        self.dataset[cue_class][cue] = self.readings
                except:
                    self.dataset[cue_class][cue] = np.vstack((self.dataset[cue_class][cue], self.readings))
            
                print(cue)
                print(self.dataset[cue_class][cue].shape)
        self.output_signal.emit('End of sessions')
        print(self.dataset.keys())
