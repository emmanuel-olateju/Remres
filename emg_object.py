import numpy as np
import serial
import time
import re

conversion_factor = 3.3 / (65535)

class emg_signal:
    def __init__(self,serial_port, epoch_time, file_name=' ', baud_rate=115200):
        self.ser = serial.Serial(serial_port, baud_rate)
        self.data_size = int(float(epoch_time)/0.001)

        if file_name != ' ':
            # print('file use')
            self.file = open(file_name+'.csv','w')
        else:
            self.file = None
        
    def clean_data(self, raw_data):
    # Use regular expression to remove non-numeric characters from the string
        cleaned_data = re.sub(r'[^\d]', '', raw_data)
        return cleaned_data

    def read(self,val=0):
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        time.sleep(0.001)
        print('sending')
        self.ser.write(bytes([1]))
        print('sent, receiving')
        self.line = self.ser.read(3)
        print('received',self.line)
        # data_str = self.line.decode().strip()
        # cleaned_data = self.clean_data(data_str)
        # temp = float(cleaned_data)
        # temp =  float(self.line.decode().strip())
        # temp *= conversion_factor
        # if self.file != None:
        #    self.file.write(str(temp)+",")
        return self.line

    def continuous_read(self,Ns=100,val=0):
        a = []
        for i in range(self.data_size):
            a.append(self.read())
        return np.array(a)


# val_print = lambda x:print(x)

if __name__ == '__main__':
    global va
    va=0
    la = emg_signal('COM8', epoch_time=2, file_name='test', baud_rate=115200)

    while True:
        data = la.continuous_read(Ns=1)
        print(data)
