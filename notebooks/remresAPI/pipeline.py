# from remresAPI.preprocessing import preprocessor
import copy

class preprocessor:
    def __init__(self,name):
        self.__name__ = name
    
    def name(self):
        return self.__name__
    
    def resetName(self,new_name):
        self.__name__ = new_name

class Pipeline(preprocessor):
    def __init__(self,name,processors):
        super().__init__(name)
        self.__processors = processors
        self.__processors_name = [p.name() for p in self.__processors]
        self.output = None
        self.results = dict()
    
    def run(self,X,y=None):
        __X = copy.deepcopy(X)
        for _processor in self.__processors:
            __X = _processor.fit_transform(__X)
        self.output = __X
        return self.output
    
    def addProcessor(self,processor,inplace=False):
        if inplace==False:
            dummy = copy.deepcopy(self)
            dummy.__processors.append(processor)
            dummy.__processors_name.append(processor.name())
            return dummy
        else:
            self.__processors.append(processor)
            self.__processors_name.append(processor.name())

    def addProcessors(self,processors,inplace=False):
        if inplace==False:
            dummy = copy.deepcopy(self)
            for processor in processors:
                dummy = dummy.addProcessor(processor)
            return dummy
        else:
            for processor in processors:
                self.addProcessor(processor)
    
