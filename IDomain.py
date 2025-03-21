from abc import ABC
from DomainElement import DomainElement

class IDomain(ABC):
    domainElements=[]
    compositeElements=[]


    def getCardinality(self)->int:
        return len(self.domainElements)

    def indexOfElement(self,domainElement:DomainElement)->int:
        if domainElement is not None and domainElement in self.domainElements:
            return self.domainElements.index(domainElement)
        return -1

    def elementForIndex(self,index:int)->DomainElement:
        if index<0 or index>=self.getCardinality():
            print('Neispravo zadan indeks!')
            return None
        return self.domainElements[index]

    def __iter__(self):
        return iter(self.domainElements)

    def getNumberOfComponenst(self) ->int:
        return len(self.compositeElements)

    def getComponent(self,index:int):
        if index>=0 and index<self.getNumberOfComponenst():
            return self.compositeElements[index]
        else:
            return None

    def __eq__(self,o):
        if o is not None:
            if o.__class__ == self.__class__:
                if o.domainElements==self.domainElements:
                    return True
        return False

