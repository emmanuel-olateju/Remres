from machine
import machine
import uos
import utime
from machine import Pin
emg_adc = machine.ADC(26)
conversion_factor = 3.3 / (65535)

class emg_signal:
    def __init__(self,adc_pin,file_name=' '):
        self.__adc = machine.ADC(adc_pin)

        if file_name != ' ':
            # print('file use')
            self.file = open(file_name+'.csv','w')
        else:
            self.file = None

    def __read(self,val=0):
        utime.sleep(0.001)
        temp =  self.__adc.read_u16()
        temp *= conversion_factor
        # if self.file != None:
        #    self.file.write(str(temp)+",")
        return temp

    def __continuous_read(self,Ns=100,val=0):
        a = []
        for i in range(Ns):
            a.append(self.__read(val))
        return a

    def send_data(self, data_list):
        # Convert the list of floats to bytes
        data_bytes = ','.join([str(val) for val in data_list]).encode()

        # Send the data through UART
        # self.uart.write(data_bytes)


val_print = lambda x:print(x)

if __name__ == '__main__':
    global va
    va=0

    led = Pin(25,Pin.OUT)
    la = emg_signal(26, file_name='test')
    uart = machine.UART(0, baudrate=115200)
    uart.init(115200, bits=8, parity=None, stop=1, tx=Pin(0), rx=Pin(1))
    # uos.dupterm(uart)

    while True:
        # data = la.__read()
        # data_bytes = ','.join([str(val) for val in data]).encode()
        # data_bytes = str(data).encode()
        # uart.write(b'hello world\n\r')
        uart.write(b'1')
        # print(la.__continuous_read(val=va))
        led.value(1)
        utime.sleep(0.5)
        led.value(0)
        utime.sleep(0.5)