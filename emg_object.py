from machine import ADC
import utime
emg_adc = machine.ADC(26)
conversion_factor = 3.3 / (65535)

class emg_signal:
    def __init__(self,adc_pin,file_name=' '):
        self.__adc = machine.ADC(adc_pin)
        if file_name != ' ':
            print('file use')
            self.file = open(file_name+'.csv','w')
        else:
            self.file = None

    def __read(self,val=0):
        utime.sleep(0.001)
        temp =  self.__adc.read_u16()
        temp *= conversion_factor
        if self.file != None:
           self.file.write(str(temp)+",")
        return temp

    def __continuous_read(self,Ns=100,val=0):
        for i  in range(Ns):
            self.__read(val)


val_print = lambda x:print(x)

if __name__ == '__main__':
    global va
    va=0
    la=emg_signal(26,'test')
    while True:
        print(la.__read(va))
