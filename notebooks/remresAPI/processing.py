from scipy.signal import stft

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