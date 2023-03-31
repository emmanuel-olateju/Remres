import machine
import utime
import numpy as np

emg_adc = machine.ADC(26)
conversion_factor = 3.3 / (65535)

class emg_signal:
    def __init__(self,adc_pin,epoch_time,file_name=' '):
        self.__adc = machine.ADC(adc_pin)
        self.data_size = int(epoch_time/0.001)
        self.data = np.empty((0,self.data_size))
        self.count = 0
        # if file_name != ' ':
        #     print('file use')
        #     self.file = open(file_name+'.csv','w')
        # else:
        #     self.file = None

    def __read(self,val=0):
        utime.sleep(0.001)
        temp =  self.__adc.read_u16()
        temp *= conversion_factor
        try:
            self.data[self.count] = temp
            self.count += 1
        except:
            readings = self.data
            self.data = np.empty((0,self.data_size))
            self.count = 0
            self.data[self.count] = temp
            return readings

        # if self.file != None:
        #    self.file.write(str(temp)+",")
        # return temp

#     def __continuous_read(self,Ns=100,val=0):
#         for i  in range(Ns):
#             self.__read(val)


# val_print = lambda x:print(x)

# if __name__ == '__main__':
#     global va
#     va=0
#     la=emg_signal(26,'test')
#     while True:
#         print(la.__read(va))
