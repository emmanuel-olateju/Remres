from scipy.signal import stft
from scipy.signal import cwt
from scipy.signal import morlet
from scipy.signal import ricker

import numpy as np

class preprocessor:
    def __init__(self,name):
        self.__name__ = name
    
    def name(self):
        return self.__name__

class STFT(preprocessor):
    
    def __init__(self,name,fs,ts=256):
        super().__init__(name)
        self.__fs = fs
        self.__ts = ts

    def fit_transform(self,X,y=None):
        return stft(X,self.__fs,nperseg=self.__ts)

def wavelet(X,widths,function):
    if X.ndim==2:
        __wt = np.empty((0,widths.shape[0],X.shape[1]))
        for i in range(X.shape[0]):
            __wt = np.vstack((
                __wt,
                cwt(X[i,:],function,widths).reshape(1,widths.shape[0],X.shape[1])
            ))
        return __wt
    elif X.ndim==1:
        return cwt(X,function,widths)

class Wavelet(preprocessor):

    def __init__(self, name,widths,function=morlet):
        super().__init__(name)
        self.widths = widths
        self.method = function
    
    def fit_transform(self,X,y=None):
        return wavelet(X,self.widths,self.method)