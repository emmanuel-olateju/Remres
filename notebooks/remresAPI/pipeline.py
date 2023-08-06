# from remresAPI.preprocessing import preprocessor
import copy

class preprocessor:
    def __init__(self,name):
        self.__name__ = name
    
    def name(self):
        return self.__name__

class Pipeline(preprocessor):
    def __init__(self,name,processors):
        super().__init__(name)
        self.__processors = processors
        self.__processors_name = [p.name() for p in self.__processors]
    
    def run(self,X,y=None):
        __X = copy.deepcopy(X)
        for _processor in self.__processors:
            __X = _processor.fit_transform(__X)
        return __X