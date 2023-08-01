from collections import deque
from add_and_shift import add_and_shift
from pylsl import StreamInfo, StreamOutlet
import numpy as np
import serial
import time

conversion_factor = 3.3 / (65535)

class emg_signal:
    def __init__(self,serial_port, epoch_time, file_name=' ', baud_rate=2000000):
        self.ser = serial.Serial(serial_port, baud_rate)
        self.data_size = int(float(epoch_time)/0.001)

        if file_name != ' ':
            # print('file use')
            self.file = open(file_name+'.csv','w')
        else:
            self.file = None

        time.sleep(4)
        
    def lsl_push(self, data):
        stream_name = "EMGStream"
        stream_type = "EEG"
        channel_count = 1 
        sampling_rate = 1000  # desired sampling rate (samples per second)
        data_format = 'float32'  # Data format

        info = StreamInfo(stream_name, stream_type, channel_count, sampling_rate)
        outlet = StreamOutlet(info)
        outlet.push_sample(data)

    def read(self,val=0):
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        time.sleep(0.001)
        self.ser.write(bytes([1]))
        self.line=self.ser.read(3)
        temp = (self.line[1]<<8)+(self.line[0]&0xff)
        temp *= conversion_factor
        self.lsl_push(temp)
        return temp

    def continuous_read(self,Ns=100,val=0):
        a = deque([0.0]*self.data_size)
        for i in range(self.data_size):
            value = self.read()
            a = add_and_shift(a, value, self.data_size)
        return np.array(a)

if __name__ == '__main__':
    global va
    va=0
    la = emg_signal('COM11', epoch_time=0.1, file_name='test', baud_rate=2000000)
    time.sleep(2)

    while True:
        data = la.continuous_read(Ns=1)
        print(data)
