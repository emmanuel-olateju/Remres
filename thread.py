import time
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal
from gui_cue_generator import cue_generator
from gui_emg_object import emg_signal

class CueGeneratorThread(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self, iterations, trials, epoch_time, file_name=' '):
        super().__init__()
        self.iterations = int(iterations)
        self.trials = int(trials)
        self.epoch_time = float(epoch_time)
        self.dataset = {}
        data_size = int(self.epoch_time/0.001)
        self.shape = np.empty((0, data_size))
        self.emg = emg_signal(26, self.epoch_time) 

        # if file_name != ' ':
        #     print('file use')
        #     self.file = open(file_name+'.csv','w')
        # else:
        #     self.file = None 

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
                self.output_signal.emit(cue)
                readings = self.emg.continuous_read()  
                # time.sleep(self.epoch_time)
                
                try:
                    if not self.dataset[cue_class].get(cue, None):
                        self.dataset[cue_class][cue] = readings
                except:
                    self.dataset[cue_class][cue] = np.vstack((self.dataset[cue_class][cue], readings))
                print(cue)
                print(self.dataset[cue_class][cue].shape)
        self.output_signal.emit('End of sessions')
        print(self.dataset.keys())
