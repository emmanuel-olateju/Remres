import numpy as np
from scipy import signal

class preprocessor:
    def __init__(self,name):
        self.__name__ = name
    
    def name(self):
        return self.__name__

class baselineCorrection(preprocessor):
    def __init__(self,name):
        super().__init__(name)

    def fit_transform(self,X,y=None):
        __mean = np.average(a=X, axis=-1)
        return (X.T-__mean).T
    
class filter(preprocessor):
    def __init__(self,name,sample_rate,low=1,high=30,order=2):
        super().__init__(name)
        self.__lowcut = low
        self.__highcut = high
        self.__nyquist_freq = 0.5 * sample_rate
        self.__low = self.__lowcut/self.__nyquist_freq
        self.__high = self.__highcut/self.__nyquist_freq
        self.__range = [self.__low, self.__high]
        self.__order = 2
        self.__filter_coeffs = self.__b, self.__a = signal.butter(self.__order,self.__range,btype='band')

    def fit_transform(self,X,y=None):
        if X.ndim==1:
            return signal.filtfilt(self.__b, self.__a, X)
        elif X.ndim==2:
            __data = np.empty((0,X.shape[-1]))
            for i in range(X.shape[0]):
                __data = np.vstack((__data,signal.filtfilt(self.__b, self.__a, X[i,:])))
            return __data