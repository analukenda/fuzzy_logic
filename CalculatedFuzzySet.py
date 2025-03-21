from IFuzzySet import IFuzzySet
from IDomain import IDomain
from IIntUnaryFunction import IIntUnaryFunction
from DomainElement import DomainElement

class CalculatedFuzzySet(IFuzzySet):
    def __init__(self,domain:IDomain,iIntUnaryFunction:IIntUnaryFunction):
        super().__init__(domain)
        if iIntUnaryFunction is not None:
            self.iIntUnaryFunction=iIntUnaryFunction
        else:
            print('Funkcija mora bit zadana!')
            exit(1)

    def getValueAt(self,domainElement:DomainElement):
        return self.iIntUnaryFunction.valueAt(self.getDomain().indexOfElement(domainElement))
