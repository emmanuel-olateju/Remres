# import machine
# import utime
import time
import random
import numpy as np

# emg_adc = machine.ADC(26)
conversion_factor = 3.3 / (65535)

class emg_signal:
    def __init__(self,adc_pin,epoch_time,file_name=' '):
        # self.__adc = machine.ADC(adc_pin)
        self.data_size = int(epoch_time/0.001)
        # self.count = 0
        # if file_name != ' ':
        #     print('file use')
        #     self.file = open(file_name+'.csv','w')
        # else:
        #     self.file = None

    def __read(self,val=0):
        time.sleep(0.001)
        # temp =  self.__adc.read_u16()
        # temp *= conversion_factor
        temp = random.random()
        # try:
        #     self.data[self.count] = temp
        #     self.count += 1
        # except:
        #     readings = self.data
        #     self.data = np.empty((0,self.data_size))
        #     self.count = 0
        #     self.data[self.count] = temp
        #     return readings

        # if self.file != None:
        #    self.file.write(str(temp)+",")
        return temp

    def continuous_read(self,Ns=100,val=0):
        data = []
        for i  in range(self.data_size):
            data.append(self.__read(val))
        return np.array(data)


# val_print = lambda x:print(x)

# if __name__ == '__main__':
#     global va
#     va=0
    # la=emg_signal(adc_pin=26, epoch_time=3)
    # r=la.continuous_read()
    # time.sleep(3)
    # print(r)
#     while True:
#         print(la.__read(va))
