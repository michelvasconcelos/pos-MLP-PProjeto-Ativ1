from abc import ABC, abstractclassmethod

class IRoute(ABC):
    @abstractclassmethod
    def path(self):
        pass
        #raise NotImplementedError()